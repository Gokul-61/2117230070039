def knapsack(capacity, vehicles):

    n = len(vehicles)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table
    for i in range(1, n + 1):

        duration = vehicles[i - 1]["Duration"]
        impact = vehicles[i - 1]["Impact"]

        for w in range(capacity + 1):

            if duration <= w:

                dp[i][w] = max(
                    impact + dp[i - 1][w - duration],
                    dp[i - 1][w]
                )

            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find selected tasks
    selected_tasks = []

    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            task = vehicles[i - 1]

            selected_tasks.append({
                "TaskID": task["TaskID"],
                "Duration": task["Duration"],
                "Impact": task["Impact"]
            })

            w -= task["Duration"]

    selected_tasks.reverse()

    return {
        "MaximumImpact": dp[n][capacity],
        "SelectedTasks": selected_tasks
    }