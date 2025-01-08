import logging
import config
from analytics import Research


def main():
    try:
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
        analytics.send_telegram_message("The report has been successfully created")
        print("Report saved successfully to report.txt!")
    except Exception as e:
        analytics.send_telegram_message("The report hasn't been created due to an error")
        logging.error("Error in main program: %s", str(e))
        raise


if __name__ == "__main__":
    main()
