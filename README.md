# Python RPA Challenge — Web Scraping and Email Reporting

A small Python automation project developed as a technical challenge. It collects public quotes from [Quotes to Scrape](https://quotes.toscrape.com/), saves them as CSV, summarizes the data with pandas, and emails the report as an attachment.

## How it works

1. Selenium opens the source website and navigates through quote pages.
2. The collected quotes, authors, and tags are written to `data/citacoes.csv`.
3. pandas calculates the number of quotes, the most frequent author, and the most common tag.
4. Python's standard `smtplib` sends a summary and the CSV file to the configured recipients.

This is a learning/challenge project, not a production integration.

## Stack

Python · Selenium · pandas · WebDriver Manager · python-dotenv · SMTP

## Run locally

Requirements: Python 3.13 (or a compatible version), Google Chrome, and a Gmail account configured with an **app password** for SMTP.

```bash
git clone https://github.com/CaioYgor28/DesafioParvi.git
cd DesafioParvi
python -m venv .venv
```

Activate the environment:

- **Windows PowerShell:** `.venv\Scripts\Activate.ps1`
- **macOS/Linux:** `source .venv/bin/activate`

Install dependencies and configure local settings:

```bash
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your own settings:

```env
URL=https://quotes.toscrape.com/
EMAIL=you@gmail.com
PASS=your-gmail-app-password
EMAIL_LIST=recipient@example.com
```

Then run:

```bash
python main.py
```

The scraper uses the Chrome browser. An internet connection is needed for the website and email delivery.

## Repository layout

```text
main.py                 Workflow entry point
src/encontrando_dados.py   Collect quotes
src/criando_csv.py         Export CSV
src/processando_dados.py   Analyze CSV
src/corpo_email.py         Build the summary
src/enviar_email.py        Send the report
data/                      Sample CSV output
.env.example               Configuration template
```

## Notes

- `.env` is ignored by Git; **never commit email passwords or recipient lists**.
- The sample `data/citacoes.csv` is example output, not evidence that the script was recently executed.
- This is a technical exercise; avoid using the configured mailbox for bulk or unsolicited email.
