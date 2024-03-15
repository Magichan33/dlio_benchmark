if __name__ == "__main__":
    import json
    import statistics

    files = [
        "2024-03-12-22-39-48",
        "2024-03-13-00-50-39",
        "2024-03-13-03-07-50",
        "2024-03-13-03-53-05",
        "2024-03-13-04-45-03",
        "2024-03-13-05-38-34",
        "2024-03-13-16-46-31",
        "2024-03-13-17-47-15",
        "2024-03-13-18-40-58",
        "2024-03-13-19-32-41",
        "2024-03-13-20-28-01",
        "2024-03-13-21-21-11",
        "2024-03-13-22-13-59",
        "2024-03-13-23-06-45",
        "2024-03-13-23-06-46",
        "2024-03-13-23-58-09",
        "2024-03-14-00-50-11",
    ]
    epochs1 = []
    epochs2 = []
    epochs3 = []
    epochs4 = []
    epochs5 = []

    for file in files:
        try:
            f = open(
                f"/mnt/disks/ssd-array/dlio_benchmark/hydra_log/unet3d/{file}/per_epoch_stats.json"
            )
        except:
            f.close()
            continue

        data = json.load(f)

        epochs1.append((data["1"]["duration"]))
        epochs2.append((data["2"]["duration"]))
        epochs3.append((data["3"]["duration"]))
        epochs4.append((data["4"]["duration"]))
        epochs5.append((data["5"]["duration"]))
        f.close()

    print(len(epochs1))
    print(len(epochs2))
    print(len(epochs3))
    print(len(epochs4))
    print(len(epochs5))
    print(statistics.mean(epochs1))
    print(statistics.mean(epochs2))
    print(statistics.mean(epochs3))
    print(statistics.mean(epochs4))
    print(statistics.mean(epochs5))
