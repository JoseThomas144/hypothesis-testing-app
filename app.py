import streamlit as st
from scipy.stats import norm, ttest_1samp

st.title("Hypothesis Testing Calculator")

st.header("One-sample Z-test")

mean = st.number_input("Sample Mean")
mu0 = st.number_input("Hypothesized Mean")
sd = st.number_input("Standard Deviation")
n = st.number_input("Sample Size", step=1)

if st.button("Run Z-test"):
    z = (mean - mu0) / (sd / (n ** 0.5))
    p_value = 2 * (1 - norm.cdf(abs(z)))

    st.write("### Results")
    st.write("Z-score:", z)
    st.write("p-value:", p_value)
