# run_tests.py
import webbrowser
import os

import pytest

if __name__ == "__main__":
    pytest.main(["--html=test_report/report.html"])

    report_path = "test_report/report.html"

    if os.path.exists(report_path):
        webbrowser.open(f"file://{report_path}")
    else:
        print("Test report not found. Please run `python test_report/report.py`")