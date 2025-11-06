import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# st.title() makes a large title at the top of the page
st.title("My Cool Dashboard!")

# st.subheader() is a smaller heading
st.subheader("An analysis of the stuff that I analyzed")

# st.write() can display plain text or variables
st.write("This app displays many interactive elements that give insight into the data I analyzed.")

# st.header() creates a section header
st.header("1. Text and Formatting")

# st.markdown() supports Markdown formatting (similar to formatting you might use with LaTex. There is also a LaTex formatting feature.)
st.markdown("""
- **Bold text**
- *Italic text*
- Links: [Streamlit website](https://streamlit.io)
""")




st.header("2. Widgets (User Inputs)")

# Text input box (default value = "Guest")
name = st.text_input("Enter your name:", "Guest")

# Slider (range: 0 to 100, default = 25)
age = st.slider("What is your age?", 0, 100, 25)

# Dropdown menu
zodiac = st.selectbox("Your star sign:", ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",  "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"])

# Display user inputs dynamically
st.write(f"Hello **{name}**! You are {age} years old and your star sign is {zodiac}!")



import pandas as pd
st.header("3. Charts and Plots")

# Random dataset (20 rows, 3 columns). When creating an actual dashboard, you will use real data.
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

# Line chart
st.line_chart(chart_data)

# Bar chart
st.bar_chart(chart_data)

# Area chart
st.area_chart(chart_data)

# Note that we can simply use a dataframe as the argument and it seamlessly creates the chart!



# You can also create plots using matplotlib

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the figure
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sine Wave")

# Display it in Streamlit
st.pyplot(fig)




st.header("4. Layout and Columns")

# Create two columns side by side
col1, col2 = st.columns(2)

with col1:
    st.write("Left column chart")
    st.area_chart(chart_data)

with col2:
    st.write("Right column chart")
    st.scatter_chart(chart_data)





st.header("5. Session State (Keeping Data for a Session)")

# Initialize counter if it doesn't exist yet
if "counter" not in st.session_state:
    st.session_state.counter = 0

# Button to increment counter
if st.button("Increment counter"):
    st.session_state.counter += 1

# Display current counter value
st.write("Counter value:", st.session_state.counter)


import time
st.header("6. Progress & Status")

# st.progress() makes a progress bar (0 to 100)
progress = st.progress(0)

# Use loop to update the progress bar
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.success("Done!")  # success message with green box


# For practical applications, you can make the progress bar align with something meaningful on the page.


st.header("7. Images and Media")

# Display an image from the web
st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxISEhASEBEVFRAPEhUQEA8QDw8PEA8PFREWFhURFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OGhAQGC0lIB8tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLSstLS0tLf/AABEIAOAA4QMBIgACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAACAwABBAUGB//EADYQAAEDAgUCBAQGAgEFAAAAAAEAAhEDIQQSMUFRBWETInGBMpGhwQYUQlKx8OHx0TNicpKy/8QAGAEAAwEBAAAAAAAAAAAAAAAAAAECAwT/xAAiEQEBAQACAwEAAgMBAAAAAAAAARECIQMSMUFRYSIycRP/2gAMAwEAAhEDEQA/AMeNbdc6rTXRxBkrI9q4+HHplWIsSytTws1QLT1Z0pxSXFG9KcjElPWd7VpclkK5CsKZTWmkxC1q0U2qywbWosqMNVkKVM72pDmrTUCzvKchVTSnsulU2ytNOmi8TjRRpBPNFDSTwosPWN9FK8O62VSs6mcRptKmtDQl0inKLxXpNRIcE6olLTjOk0hwUaEwoCnhGAKFippTAVOYsvw1E1RLaWR0nlJcnuahyLX1HsyOakVKS6BpoDSQnXKdRSzSXWNBCcOjonIdSQ+Eut+WVHCpwY5jaSfTprWMOiFFOmz5VRatXhKjTUhhexIdSXTNJAaKNKsjKaexqMMRtaq0IAmBW1qPKpFIeFnK1vakuanhLplNDlnDU0KF6jyghHCvKqIhwSiFpcEkhAUxNCANRgJ0xSohUU5Bru5VWRMUVs9L8NTw0atRS0s01XhJysKD0oUVRorUAoQunx/FRidRSzTWx6UQl5KLSDTQeGtMKZVlC1m8NC6ktgYqcxOlrnOpoQFtfTS/CQNLaEeVGGK8qRWkOagNNasiosTErL4ahatBYgIUVWkhqhCYVUJSjSXNSiFqLUssV6elNaiIR5FRCBoIURKIN2gUYCWE1qqVikKQjARQigrKrATIV5VOAAVkqyFUKpbD0pyGE7KpkSvZaRlVgJ+RQtU4NJAV5UyF1OidLNVwd+lrhm9FXGW3D+sGE6ZUqZcrSQ46xZdQfg6sQbjsF7nC4VlJoDQAGiyM4gLb1n8Np4p+18ux/SKlIw4X7ccrEGL6R+JqjRRcSLm2wnsV89IWHlnremXOetwktS3BaC1Lc1Rx5dlKQQhLU/IrFNa8ssFrG5igprYaasU1lo1mbSUNFbmU1HU0aHNdTQOYt76aU6mmrjWLIotPhqJqapRNclqwmyPa9GHrMHK8yek1ByvMswejDk4DpUBSsymdMHIpSA9WHoBpKolLzqsyYGvdfhOgG0cw1dr6heEYbhfSeksApMjdonvZVwn1r4Z/kPFVdgsONrGnTdUN8o00Wmt8SrH4bxKTmxtPutvkaXbrwvUepVKx85ts3YLCU/FUyHEHUH+Ekrk5cbb25dAqyoioFn6jVZVIRFCUWU9RSUMoS5Rg00OVl6zFyqUoNPKAtVNKKVpKcoPDVopUVaelhXKz50TXo1JqkIQUQciUUTQjAQSoHKoWiUUCsJhQVo2tV5UwWArhG0IoS0Bpi6+kdEqTRZeYEHkL51T1HqvpHSCDSYYAMXhacPjXw/7ArarRSMhKxTeEWGK2/G0+vIfiTCZanlFjoBt3K4bgvovVcEKjT2E/75XgsVQLSQZJBvxKy5z9c3k4+tZSpChRBqwSGFC1HCtAILUJatEKsqWBmLFMi0ZVUJXiCwxU9qcgeozDhSiOFSAzNpKwxG2orBWhghG1qhVhyNSIsVhqhehD09A4UBS3FUCn9DS0oi5Z2FEZT+AeZTMhDSnUcK51mgk7AehKJLSRgXu/wtiCaeU6t35C850vodRzhLSBudF7PpfThRbGq148fWdtvDxvtplZiRTst7glOYFc5Oi8UbcLyH4vw2UtcLA2gfyvWNMLF1nBeKwiQO5Ex6Iz8R5JvF86lMaUeLw+RxA00nlIlYXi5TihKDMqL1ODRAq5SpUzIGHhA5BnUzIGLlWAhlWHJYBZFFPEURkJy2FOBWVpTGkpWdNLGpAhDpRQo42pGAoGoHPQPrJXbSw0lWAk0pJWp7IVTTxo6U4CqyXFozCSLwPTdfSXYSk4QabC0j9jb91856U2iXDxXuaQbHKC09ivofTKjHsBpulotN/uurxzpr4fuFU/w/hwSclj+kkwFtw+ApsjK0CNFYdCM1FWVvOPGfhwhQuCx1K65eLxbi7KPhAkkkgf5T4+O07zkdoYhpMDXXsheVzMBUkk7aBbn1FV4ZUzlsWSo07cpOZTOnha89+IunwLXi68xlX0LqFHOwngac9l4DEAhzgRF9Fl5J+ufnxygyqsiherzrC0s6DlV5ULTdG4KfZJbwlNctAeIhILFezDWXIS5VCpyVIWZRKzKIygulTlMay6CoS0KNq2UTkoQbBTMyW0ndUJBR/08OyyiqYbSEFN100VLqf1KNZl1VOfKqpVzICYsi9Bt6VhvEe1t7nYA/yvp2Dw7aTGtGwvoLr5r0LFmnVaWBuZ3lDnz5Z34X0qoYaLk2uTqTyurxZeLbw5NoMTWDWucQYaCTHAXNwPWqdYkU9RNjGxIJEG9wQtf5lpOU3m0crM+hRoB1SnS8wFw2MxbxJOnZdMkk7na7bb1Seo9Rp0sviOgX2JJIBJgDsCUvD16ddocx2Zh3vBSadOlixnrUnBo/6ZccriDqWwZATM9NgbSpABrdGi/wA1pMzpndl7baLQ0Wt6WCYai5zcRNk5r0eonJpL1XiLO96UaqPUvZ08NX+q8d+JnDxrcfVd1uIg6ry/W64fVJboOFh55kLly2YwvRNbZQgQkGuJhck4py05joQGtJQQZsmBsWT9YWBF0TDyo0x6Jb3XsqwGboiwJY5R0nyYSz8FkTwFFr8NRHqPWuTXfmiN1VDeNkVN2/CFtImT725WXDjnUP6F75P8poKlLAEsc/MLH4SboJAA3+yfLhf0Cc4xKKuYEhEw/wCkp9YZoi33U/AlNx4RPpmJn2UqVNY3UosN5Ponc/Ro8LVgzoWmQRyNF9O6ZihWotdvEHa/C+Z1IaIy3+q9P+EerNafCe4AG4m2uy28N/FePlldrFYYgyNdVyepF5BBJje8SvS4tm401XExTOV28bsPnMrkUK1VgDWiGiwBJNo/wm0S4OLpudRFit/hiEkm49U9rPDKdSYJT2vWFhh0bESO0a/yPqnOqgKxp1asFlqV1zcf1ANME34GpXOPUc2mn1hRy8vHiXdbepdQiQDdculrJTM7XE7lKqNAgg+3C4Ofk9uWnBwYJWejh58xTPzHy4RNMi2iNyKl/lTqkFbMO0FpzbpdFgLTOo3KxY/HFo8okN1j9R4U8eU1U4+3UahSlp7aJVKncTum4TENcGzvqPVECMwnQLTYiyxmrggwOfmra0iCNeFrfUaDPNgOVK4a1wIMgifRK3NpyXNLyP8A6VEj852+qtT7/wBF2VkOU8jQ203Sw45SBoD7k7oajGwGskTLczrgOF80cSfkl0Kbg1znWI1bBIDt8p0y99ln+idmVakDKdSYjeeUZxMlrSLxfYwNSsZDTUgiXzmZBtJAc62y0hrvhe2HgTG8TBBHzt2Kc7k1XKT8Rj3OmAOB6zEq3UssvFxbfblBSabWkG1hYHbT+2Kc1zYg8BsR7b/26VQrI4Bz3WH6W7lL8UuDgPiF2zYE7t9lr8IuIl8gu+ECMrQPhHbVDiw2PLHqbw7YD1lPnxn2fSlI8Z4yue3XuJkJD8ac0u11FtWp1SYBIl4HIyttxvyo4tezhzXEB0WbOrfb7rOap9E6V1dtShTMjO1oa9vBA/xolHFhxM6jTuD/AKK8HTrmmRlcRAylzZyuE/C4b+60u6tVDrAG0C+xj5xC7uHmkn+R269XWxILsoNzZF4Qm8y7+Rf57+xXP/DYdVIcTDnC2ZhMx8UCQunjXxID2lzcr2xRqXOgEh0CYy+5XROUs1LO4wYdZzXA9nNd5Z+t/wDIXI6p1VrXFodJgiN2m0rR1TqANPMNxLXNkSbWgjcEW7dl5KsC4uLgJlxMa3beO1lHl8nrMn6JNXiK4LgZ9ymtd+oiOR91zm0/MXbQMjSTsIPvELWwkAWJa4EtB+OJgjuBodtNJC4puLaqFXzWsCCZtwYRvqbTbc/uP/C5rXBliR5pIO2W3/P0T6bwRB1mDfvqj4XS3VPN2IEfRXReToTrETCge3zQ24ETwdf+E0VG5pGvHtdyOPObgMFTUA7E39JhLjySG+UG49U6q8S0kDQgWvOg+/yT6BtlEAkEi8mBcf8AzCXtvwmWmHZCRyI/1qpVe6+ok22tAP3TPCkgB5mf1GZAN9PVNewh0RtDSAIbMxHPM9ldsDK2qco7G33+yY5odOU+Z9yP3enCHEVQIAu0SPKQYIInNvOiJpDS0j4dZtPuOR3R7T9OfF/lex+RVJ35537m/wDq5RP/ANPGGQtAhpnzXHfS/wA5+aNtL4iLZtIuYJE29ilhufLtGnZMDPic250sduB8llZBhbaPmJaBnlskROUfSYT8QJl3sYgcg/zKKnRyj/yGpuZ2RCnrPvxKnlP7FqsNT8mozQbkRAJMabxuluoSYmwv6+qdSpF3wkQNZtKTUqQSB/eyLqRVKrbxMbm152V5rDKScsw0xGbcrMGSbmBAgfdMr1wIAHaO3KU6GCyadttYm5J+qAUz5abrAAZiTfzakc2ATqLmxmOosjcAddxvf0VYNukVGtgsbMBxvrJnn5rDWqta/KLSb6xxY8rVXpnyhkgyDbhaqkZIiHEa9+VWSYcsgR1CowUyxxb4Z8oiwLrAwO1rrMOqvc7PmiHZjeQ3M4kiD/3A27hGA7Wd4c39wShSABtNvcnlVOd+Uia1Qgk7AkgbSRefdFhaMi+kdxBnQeydXpj4uBJjUmArw9InYga3I07pc+zvwurh2tbbWQBOwn/H1T6TiGkyA0uhjToBBuOL7ofCJfB0kFQjNI/S2wvqOD3Tm0fVPw1N+aBdzTNM6DcOb6ED5LBQoG7HawTmLY12t6D5Lo1DlGskDYDXcpeErXvNxlvsCIlX1R/bHSojMSXFwcM4AGpA+KfSBC0UXagDW510H3TWsDOLiCI53TKdJwbpIjcWO11M4T4e/wAM9LEblpzZcsjidCPcp9JzQ2ZMj9XvNiNoUqZQ2HXdYNA43HyS230MAQefaeUXh39Kn4avAcYk5tDrmDYcL6iB/YWWljTInQa3B/u3zTXnWJjU2gzOtrIXXMmJGjuY0JHIS9f0hve2agNpJh4g31ntaPkE19O95ylokx+qJJ11kqvABGWZBiNZF1DUexxBcLGzTcObxbRF7sOS1fgd/wC/JRP/ADdP9iifX8jayUnCFG2tss4fZQVpUU2t0m822Vl8hZm1CoKh9lNm9ka+tqAqpHMeN0BiVRsZCXUNdd0JDa4JHKcSHaoadEAq7JOO10evGcNx0HskWQl3GyFlQQrgQVnLNcqPIgHfsibUBEHRLDxCGAUTnvQLDbmNroabnRJ5Wo0YgoANUX4cONMFoPusviRMHVaRpCz1Kd0e34RzXWvuhY2NkbG8oXOJVbSE5mnOytkCOf5S6phIpEi5WsNsFMAlx1Og1CCuTIzGeyU6sZE6Kq1STKLcLtnxTvMLeioPAE87K8Q1ztNkmjQcRdTZq+jGPgn+grTSbuYgXSvA0CvFUyIAT7wjKlQzP8IW+eSbnugptMa3VYcHROfNMUf2VEeUK0b/AETG4IWtuhL1M6n6qnh6h7JITQo7gLYDKJ1QpwcFHAaoyW6TKxjputVKnKE1wjoVhMqby/D2mtw5mUcnRG+vMI36SsZaTK50KUqt0FR6qg1a50cbS0lHTpAaoaVTYpjhKPbPqajmjVJDmpeMJiyx0WHdV0rJjreK1ZsQ6NEGHoklOrUbXSmTpnjPTq8pDqhLuyY8pS24yRYsbWIFleH7qg0lNpiLJ4X4XXeQbI6Lt0vFXUpttCrJBnTTRqyU2rT73WJzSNEulUINysr9BuWCqaSCmNcClvdJVTl3gNlWkKLQ8f/Z", caption="Cute kitten 😺")

# Embed a video
st.video("https://www.w3schools.com/html/mov_bbb.mp4")


st.header("8. Putting Everything Together")

st.write("You are a competitive chess player. You are about to play in a chess tournament, but you want to first know how your chess ELO rating could change and what your prospects look like.")

user_rating = st.number_input("What is your current rating?", value=1200)
games = st.number_input(
    "How many games/opponents in your tournament?",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

new_cols = st.columns(games)

ratings = []
for i, col in enumerate(new_cols):
    with col:
        rating = st.number_input(
            f"Opponent {i+1} rating",
            min_value=0,
            max_value=3000,
            value=1200,
            step=10,
            key=f"rating_{i}"
        )
        ratings.append(rating)

# Elo update function
def elo_update(Ra, Rb, outcome, K=32):
    # outcome = 1 if win, 0 if loss
    Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
    return Ra + K * (outcome - Ea)

opponent_ratings = ratings

st.subheader("Expected Points per Game (Elo)")

rows = []
Ra = user_rating

for i, Rb in enumerate(opponent_ratings):
    Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))  # expected points this game (0..1)
    rows.append({
        "Game": i + 1,
        "Opponent Rating": Rb,
        "Expected Points (0–1)": round(Ea, 4)
    })

exp_df = pd.DataFrame(rows)
st.dataframe(exp_df, use_container_width=True)

# Summary stats
expected_total_points = exp_df["Expected Points (0–1)"].sum()
expected_score_pct = 100 * exp_df["Expected Points (0–1)"].mean()

st.markdown(f"**Expected total points:** {expected_total_points:.2f} / {len(opponent_ratings)}")
st.markdown(f"**Expected score percentage:** {expected_score_pct:.1f}%")


if opponent_ratings:
    # All wins scenario
    rating_all_wins = [user_rating]
    Ra = user_rating
    for Rb in opponent_ratings:
        Ra = elo_update(Ra, Rb, outcome=1)
        rating_all_wins.append(Ra)

    # All losses scenario
    rating_all_losses = [user_rating]
    Ra = user_rating
    for Rb in opponent_ratings:
        Ra = elo_update(Ra, Rb, outcome=0)
        rating_all_losses.append(Ra)

    # Summary
    st.subheader("Results")
    st.write("Maximum rating after tournament:", round(rating_all_wins[-1]))
    st.write("Minimum rating after tournament:", round(rating_all_losses[-1]))

    # Approximate distribution after tournament (probabilities)
    Ra = user_rating
    prob_distribution = {}
    def dfs(i, Ra, prob):
        if i == len(opponent_ratings):
            prob_distribution[round(Ra)] = prob_distribution.get(round(Ra), 0) + prob
            return
        Rb = opponent_ratings[i]
        Ea = 1 / (1 + 10 ** ((Rb - Ra) / 400))
        # Branch win
        dfs(i+1, elo_update(Ra, Rb, 1), prob * Ea)
        # Branch loss
        dfs(i+1, elo_update(Ra, Rb, 0), prob * (1 - Ea))
    dfs(0, user_rating, 1.0)

    dist_df = pd.DataFrame(list(prob_distribution.items()), columns=["Rating", "Probability"]).sort_values("Rating")

    # Plot progression lines
    fig, ax = plt.subplots(figsize=(7,5))
    ax.plot(range(len(rating_all_wins)), rating_all_wins, label="All Wins", color="green")
    ax.plot(range(len(rating_all_losses)), rating_all_losses, label="All Losses", color="red")
    ax.set_xlabel("Games")
    ax.set_ylabel("Rating")
    ax.legend()
    st.pyplot(fig)

    # Plot probability distribution
    st.subheader("Final Rating Probability Distribution")
    st.bar_chart(dist_df.set_index("Rating"))