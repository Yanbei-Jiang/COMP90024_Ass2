import yaml
from model.RumourDetector import RumourDetector


def train(model, configs):
    pass


def main():
    with open("./config.yml", 'r') as f:
        configs = yaml.load(f, Loader=yaml.FullLoader)
    model = RumourDetector(configs)
    train(model, configs)


if __name__ == "__main__":
    main()
