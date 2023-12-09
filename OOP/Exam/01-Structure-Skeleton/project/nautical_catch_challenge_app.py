from project.divers.free_diver import FreeDiver
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        valid_diver_types = ["FreeDiver", "ScubaDiver"]

        if diver_type not in valid_diver_types:
            return f"{diver_type} is not allowed in our competition."

        for diver in self.divers:
            if diver.name == diver_name:
                return f"{diver_name} is already a participant."

        if diver_type == "FreeDiver":
            diver = FreeDiver(diver_name)
        else:
            # Handle ScubaDiver creation if needed
            pass

        self.divers.append(diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        valid_fish_types = ["PredatoryFish", "DeepSeaFish"]

        if fish_type not in valid_fish_types:
            return f"{fish_type} is forbidden for chasing in our competition."

        for fish in self.fish_list:
            if fish.name == fish_name:
                return f"{fish_name} is already permitted."

        if fish_type == "PredatoryFish":
            fish = PredatoryFish(fish_name, points)
        else:
            # Handle DeepSeaFish creation if needed
            pass

        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        fish = next((fish for fish in self.fish_list if fish.name == fish_name), None)
        if fish is None:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered_count = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                recovered_count += 1

        return f"Divers recovered: {recovered_count}"

    def diver_catch_report(self, diver_name: str):
        diver = next((diver for diver in self.divers if diver.name == diver_name), None)
        if diver is None:
            return f"{diver_name} is not registered for the competition."

        report = f"**{diver_name} Catch Report**\n"
        for fish in diver.catch:
            report += f"{fish.fish_details()}\n"

        return report.strip()

    def competition_statistics(self):
        healthy_divers = [diver for diver in self.divers if not diver.has_health_issue]
        sorted_divers = sorted(healthy_divers, key=lambda x: (x.competition_points, len(x.catch), x.name), reverse=True)

        stats = "**Nautical Catch Challenge Statistics**\n"
        for diver in sorted_divers:
            stats += f"{diver}\n"

        return stats.strip()
