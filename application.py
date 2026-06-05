import streamlit as st
import pandas as pd
import random
from datetime import datetime

st.set_page_config(page_title="Dine-Ease", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Poppins', sans-serif;
}

/* Background */
body {
    background: linear-gradient(135deg, #fff3e0, #ffd180);
}

/* Floating icons */
.floating {
    position: fixed;
    font-size: 55px;
    animation: float 8s infinite ease-in-out;
    opacity: 0.35;
    z-index: 0;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-60px); }
    100% { transform: translateY(0px); }
}

/* Card */
.card {
    background: rgba(255,255,255,0.9);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    backdrop-filter: blur(10px);
}

/* Title */
.title {
    text-align: center;
    font-size: 52px;
    font-weight: 800;
    background: linear-gradient(90deg, #ff6600, #ff3d00);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Tagline */
.tagline {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 20px;
}

/* Buttons */
.stButton>button {
    background: linear-gradient(90deg, #ff6600, #ff3d00);
    color: white;
    border-radius: 12px;
    padding: 12px 24px;
    font-weight: 600;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #e65c00, #d84315);
}

/* Ensure content is above floating icons */
section.main > div {
    z-index: 1;
}

</style>

<!-- Floating Icons -->
<div class="floating" style="left:5%; top:10%;">🍕</div>
<div class="floating" style="left:85%; top:15%;">🍔</div>
<div class="floating" style="left:15%; top:60%;">🍟</div>
<div class="floating" style="left:75%; top:75%;">🍩</div>
<div class="floating" style="left:40%; top:20%;">🌮</div>
<div class="floating" style="left:60%; top:50%;">🍜</div>
<div class="floating" style="left:30%; top:80%;">🍗</div>
<div class="floating" style="left:90%; top:60%;">🍦</div>

""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title"> Dine-Ease 🍽️</div>', unsafe_allow_html=True)
st.markdown('<div class="tagline">Order Faster • Serve Smarter • Win Bigger 🚀</div>', unsafe_allow_html=True)

# ---------- MENU ----------
menu = {
    "Pizza": 299,
    "Burger": 199,
    "Pasta": 249,
    "Sandwich": 149,
    "French Fries":99,
    "Chocolate Cake":179,
    "Italian Pasta":999,
    "Veggie Burger":849,
    "Grilled Paneer Tikka":599,
    "Garlic Bread":299,
    "Chicken Seekh Kebab":699,
    "Mushroom Masala":549,
    "Paneer Pizza":699,
    "Cold Coffee":199,
    "Cold Coffee":499,
    "Tomato Soup":399,
    "Veg Sandwich":349,
    "Pasta Alfredo":899,
    "Masala Chai":149,
    "Veg Burger":399,
    "Cheese Garlic Toast":299,
    "Lemon Iced Tea":149,
    "Dal Dhokli":399,
    "Undhiyu":599,
    "Khakhra":149,
    "Fafda Jalebi":199,
    "Handvo":249,
    "Khandvi":199,
    "Dhokla":149,
    "Thepla":149,
    "Pasta":499,
    "Falafel":399,
    "Oreo Shake":299,
    "Mojito":199,
    "French Fries":149,
    "Cold Drink":50

}

# ---------- LAYOUT ----------
col1, col2 = st.columns([2, 1])

# ---------- ORDER FORM ----------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🛒 Place Your Order")

    name = st.text_input("Your Name")
    item = st.selectbox("Select Food", list(menu.keys()))
    quantity = st.slider("Quantity", 1, 10)
    city = st.text_input("📍 City")
    address = st.text_area("🏠 Address")
    payment = st.radio("💳 Payment", ["Cash on Delivery", "UPI", "Card"])
    rating = st.radio("⭐ Rate Your Experience", [1, 2, 3, 4, 5], horizontal=True)

    if st.button("🚀 Place Order"):
        price = menu[item]
        total = price * quantity
        delivery = random.randint(20, 45)

        # Payment simulation
        if payment != "Cash on Delivery":
            st.info("Processing payment...")
            st.success("✅ Payment Successful!")

        new_data = pd.DataFrame([{
    "Name": name,
    "Item": item,
    "Quantity": quantity,
    "Total": total,
    "City": city,
    "Address": address,   # ✅ added
    "Payment": payment,   # ✅ added
    "Rating": rating,
    "Time": datetime.now()
}])

        try:
            old = pd.read_csv("orders.csv")
            df = pd.concat([old, new_data], ignore_index=True)
        except:
            df = new_data

        df.to_csv("orders.csv", index=False)

        st.success(f"✅ Order Placed Successfully! Total ₹{total}")
        st.info(f"🚚 Delivery in {delivery} minutes")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- DASHBOARD ----------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Live Stats")

    try:
        df = pd.read_csv("orders.csv")

        st.metric("Total Orders", len(df))
        st.metric("Revenue", f"₹{df['Total'].sum()}")

        st.bar_chart(df["Item"].value_counts())

    except:
        st.info("No data yet")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- ORDER HISTORY ----------
st.markdown("## 📋 Order History")

try:
    df = pd.read_csv("orders.csv")
    st.dataframe(df, use_container_width=True)
except:
    st.warning("No orders available")