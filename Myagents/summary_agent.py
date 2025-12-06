class SummaryAgent:
    def __init__(self, schedule_df, goal):
        self.schedule_df = schedule_df
        self.goal = goal

    def summarize(self):
        # Count study vs revision sessions
        study_sessions = self.schedule_df[self.schedule_df["Type"] == "Study"]
        revision_sessions = self.schedule_df[self.schedule_df["Type"] == "Revision"]

        topics_study = study_sessions["Topic"].unique()
        topics_revision = revision_sessions["Topic"].unique()

        total_sessions = len(self.schedule_df)
        total_study = len(study_sessions)
        total_revision = len(revision_sessions)

        summary_text = f"""
📚 **Study Plan Summary**

🎯 **Goal**: {self.goal}

📝 **Total Study Sessions**: {total_sessions}  
   - Study: {total_study}  
   - Revision: {total_revision}

📘 **Topics Covered**:
- Study Topics: {', '.join(topics_study)}
- Revision Topics: {', '.join(topics_revision)}

This schedule balances learning + revision, focusing more on difficult topics for better retention.
"""
        return summary_text