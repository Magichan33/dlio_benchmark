if __name__ == "__main__":
    import json
    import statistics

    files = [
        "2024-03-21-20-47-43",
        "2024-03-21-20-42-03",
        "2024-03-21-20-36-29",
        "2024-03-21-20-30-59",
        "2024-03-21-20-25-28",
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
            continue

        data = json.load(f)

        epochs1.append(float(data["1"]["duration"]))
        epochs2.append(float(data["2"]["duration"]))
        epochs3.append(float(data["3"]["duration"]))
        epochs4.append(float(data["4"]["duration"]))
        epochs5.append(float(data["5"]["duration"]))
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
