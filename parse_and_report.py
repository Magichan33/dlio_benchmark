if __name__ == "__main__":
    import json
    import statistics

    files = [
        "2024-03-20-21-40-59",
        "2024-03-20-21-40-58",
        "2024-03-20-20-55-06",
        "2024-03-20-20-08-41",
        "2024-03-20-19-22-01",
        "2024-03-20-18-35-00",
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
