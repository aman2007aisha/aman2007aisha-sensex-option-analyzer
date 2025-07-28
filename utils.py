def analyze_options(df):
    # Filter Call and Put data
    calls = df[df["Type"] == "Call"].copy()
    puts = df[df["Type"] == "Put"].copy()

    # Scoring undervaluation: low IV and high OI change
    calls["Score"] = (1 / (calls["IV"] + 0.01)) * calls["Change_OI"]
    puts["Score"] = (1 / (puts["IV"] + 0.01)) * puts["Change_OI"]

    calls_sorted = calls.sort_values(by="Score", ascending=False).head(5)
    puts_sorted = puts.sort_values(by="Score", ascending=False).head(5)

    return calls_sorted[["Strike", "LTP", "IV", "OI", "Change_OI", "Score"]],            puts_sorted[["Strike", "LTP", "IV", "OI", "Change_OI", "Score"]]