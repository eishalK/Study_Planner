import pandas as pd

class CalendarAgent:
    def __init__(self, topic_order, weights, time_slots, all_days):
        self.topic_order = topic_order or []
        self.weights = weights or []
        self.time_slots = time_slots or {}
        self.all_days = all_days or []

    def create_calendar(self):
        schedule = []

        # Flatten all hours across all days
        all_slots = []
        for day_key in self.all_days:
            hours = self.time_slots.get(day_key, [])
            if hours:
                if "_" in day_key:
                    week, day = day_key.split("_")
                    week = week.replace("week", "Week ")
                else:
                    week = "Week 1"
                    day = day_key
                for hour in hours:
                    all_slots.append((week, day, hour))

        if not all_slots or not self.topic_order:
            return pd.DataFrame(columns=["Week", "Day", "Hour", "Topic"])

        # Assign topics sequentially to each hour
        topic_index = 0
        num_topics = len(self.topic_order)
        for week, day, hour in all_slots:
            topic = self.topic_order[topic_index % num_topics]
            schedule.append({"Week": week, "Day": day, "Hour": hour, "Topic": topic})
            topic_index += 1

        df = pd.DataFrame(schedule)
        return df
