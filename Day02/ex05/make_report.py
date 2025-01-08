import config
from analytics import Research


def main():
    research = Research("data.csv")
    data = research.file_reader()
    
    analytics = Research.Analytics(data)
    
    heads, tails = analytics.counts()
    head_fraction, tail_fraction = analytics.fractions()
    predictions = analytics.predict_random(config.num_of_steps)
    
    predictions_text = ', '.join(
        f"{pred[1]} tail and {pred[0]} heads" for pred in predictions
    )
    
    report = config.report_template.format(
        total=len(data),
        tails=tails,
        heads=heads,
        tail_fraction=tail_fraction,
        head_fraction=head_fraction,
        steps=config.num_of_steps,
        predictions=predictions_text,
    )
    
    analytics.save_file(report, "report", "txt")
    print("Report saved successfully to report.txt!")


if __name__ == "__main__":
    main()
