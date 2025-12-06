import pandas as pd

class RevisionAgent:
    def __init__(self, schedule_df, difficulty):
        self.schedule_df = schedule_df.copy()
        self.difficulty = difficulty

    def add_revision(self):
        rows = []

        for _, row in self.schedule_df.iterrows():
            # Original study row
            study_row = row.copy()
            study_row["Type"] = "Study"
            rows.append(study_row)

            # Add revision if topic is hard (difficulty >=4)
            topic_name = row["Topic"].replace(" (Revision)","")  # clean name
            if self.difficulty.get(topic_name, 3) >= 3:
                revision_row = row.copy()
                revision_row["Topic"] = f"{topic_name} (Revision)"
                revision_row["Type"] = "Revision"
                # Optional: you can adjust Hour if needed
                rows.append(revision_row)

        return pd.DataFrame(rows)
