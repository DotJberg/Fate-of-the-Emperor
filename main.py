import random


def ChooseDeployment() -> str:
    deployments = ["Tipping Point", "Hammer and Anvil", "Search and Destroy", "Crucible of Battle", "Sweeping Engagement"]

    return random.choice(deployments)


def ChoosePrimaryMission() -> str:
    missions = ["Take and Hold", "Supply Drop", "Linchpin", "Scorched Earth", "Hidden Supplies", "Puge the Foe", "Terraform"]

    return random.choice(missions)


print("=== Warhammer 40K Mission Generator ===")
print(f"Deployment:      {ChooseDeployment()}")
print(f"Primary Mission: {ChoosePrimaryMission()}")
