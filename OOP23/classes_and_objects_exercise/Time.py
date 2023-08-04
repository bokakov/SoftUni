class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.set_time(hours, minutes, seconds)

    def set_time(self, hours, minutes, seconds):
        self.hours = max(0, min(hours, Time.max_hours))
        self.minutes = max(0, min(minutes, Time.max_minutes))
        self.seconds = max(0, min(seconds, Time.max_seconds))

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours = (self.hours + 1) % (Time.max_hours + 1)
        return self.get_time()
