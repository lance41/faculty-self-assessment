import streamlit as st

# Define groupings and focus areas
groupings = {
    "Adapter": "Building Digital Fluency",
    "Innovator": "Reimagining Learning Experiences",
    "Catalyst": "Empowering Leadership and Inspiration",
    "Collaborator": "Shaping the Future of Education"
}

# Self-assessment questions
competency_questions = [
    "How confident are you in integrating AI tools and analytics into your teaching practice to enhance student engagement and assessment?",
    "How confident are you in designing and implementing immersive learning experiences using Extended Reality (XR), gamification, or AI-driven adaptive learning?",
    "How confident are you in leading and inspiring students in technology-enhanced learning innovations and digital pedagogy?",
    "How confident are you in co-creating EdTech innovations, interdisciplinary projects, or student-industry collaborations?"
]

needs_questions = [
    "Do you want to develop skills in AI-enhanced teaching, digital assessment, and learning analytics?",
    "Do you want to enhance your ability to design immersive learning experiences using XR, gamification, or adaptive learning?",
    "Are you seeking to strengthen your leadership and inspiring abilities in EdTech and digital learning innovation?",
    "Are you interested in building collaborations, interdisciplinary partnerships, or faculty-student co-creation initiatives?"
]

interests_options = {
    "Adapter": "AI tools, analytics, and digital assessment for personalized learning",
    "Innovator": "Designing immersive and interactive learning experiences with emerging technologies",
    "Catalyst": "Inspiring students, leading student innovation projects, and fostering a culture of digital learning",
    "Collaborator": "Collaborating with students and industry partners to co-create the future of education"
}

# Define weights for competency and needs questions
competency_weights = {
    "Adapter": [0.4, 0.3, 0.2, 0.1],  # Higher weight on foundational skills (AI tools, analytics)
    "Innovator": [0.2, 0.4, 0.2, 0.2],  # Higher weight on immersive learning design
    "Catalyst": [0.1, 0.2, 0.5, 0.2],  # Higher weight on leadership
    "Collaborator": [0.1, 0.2, 0.2, 0.5]  # Higher weight on collaboration
}

needs_weights = {
    "Adapter": [0.5, 0.3, 0.1, 0.1],  # Higher weight on AI-enhanced teaching
    "Innovator": [0.2, 0.5, 0.2, 0.1],  # Higher weight on immersive learning design
    "Catalyst": [0.1, 0.2, 0.5, 0.2],  # Higher weight on leadership
    "Collaborator": [0.1, 0.1, 0.2, 0.6]  # Higher weight on collaboration
}

# Function to calculate weighted scores
def calculate_weighted_scores(scores, weights):
    return sum(score * weight for score, weight in zip(scores, weights))

# Streamlit App
st.title("Faculty Self-Assessment for Innovation in Teaching PD Series")
st.write("Assess your competencies, needs, and interests to receive a recommended grouping for professional development.")

# Competency Assessment
st.subheader("Competency Assessment")
competency_scores = []
for q in competency_questions:
    score = st.slider(q, 1, 4, 2)
    competency_scores.append(score)

# Needs Assessment
st.subheader("Needs Assessment")
needs_scores = []
for q in needs_questions:
    score = st.slider(q, 1, 4, 2)
    needs_scores.append(score)

# Interests Selection
st.subheader("Interest Areas")
selected_interests = st.multiselect("Select all that apply:", list(interests_options.values()))

# Calculate weighted scores for each grouping
grouping_scores = {}
for group in groupings:
    competency_weighted = calculate_weighted_scores(competency_scores, competency_weights[group])
    needs_weighted = calculate_weighted_scores(needs_scores, needs_weights[group])
    grouping_scores[group] = (competency_weighted + needs_weighted) / 2  # Average of weighted scores

# Adjust scores based on selected interests
for group, focus in groupings.items():
    if interests_options[group] in selected_interests:
        grouping_scores[group] += 1  # Add a bonus for matching interests

# Determine the recommended grouping
recommended_grouping = max(grouping_scores, key=grouping_scores.get)

# Display Recommendation
st.subheader("Your Recommended Grouping:")
st.markdown(f"### **{recommended_grouping}: {groupings[recommended_grouping]}**")
st.write(f"Based on your responses, we recommend you explore courses under the **{recommended_grouping}** grouping.")

# Display weighted scores for transparency
st.subheader("Weighted Scores for Each Grouping:")
for group, score in grouping_scores.items():
    st.write(f"- **{group}**: {score:.2f}")

# Allow faculty to explore other groupings
st.subheader("Explore Other Groupings")
for group, focus in groupings.items():
    if group != recommended_grouping:
        with st.expander(f"Explore **{group}** Grouping"):
            st.write(f"**{group}:** {focus}")
