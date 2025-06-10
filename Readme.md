# FHIR Longitudinal Patient Timeline Generator

The amount of EHR data that is generated each year is growing exponentially while time alloted to direct patient care is shrinking.
All healthcare providers (not just physicians) are overloaded with information yet still must make accurate decisions, often on brand new patients with complex histories.
This project reads patient information given in FHIR format (as would be provided from an EHR) and generates a visual timeline of the patient's health conditions.
This enables providers to quickly gain a holistic view of the patient's health status to make better clinical decisions.  This directly leads to
lower costs due to a reduction in redundant tests, less mental strain on providers, and more efficient healthcare.  Because this tool operates at the FHIR level, it can be used
in any healthcare information system.


## Features

- Extracts patient information from a patient whose clinical data is given in FHIR format.
- Creates a visual timeline of the patient's health conditions.

## Setup

1. Install dependencies: pip install -r requirements.txt
2. Make a virtual environment: python3 -m venv fhir_timeline (you can use any name you want;
   here it is "guidelines_rag")
3. Activate the virtual environment you just created: source fhir_timeline/bin/activate
2. Set up environment variables:
    - `OPENAI_API_KEY`: Your OpenAI API key
    - `GEMINI_API_KEY`: Your Google Gemini API key
3. Switch into the `src` directory: cd src
4. Run the main script: python main.py

## Usage

1. Provide a patient's clinical notes when prompted.
2. The system will extract patient information and retrieve relevant screening test guidelines 
based on the US Preventive Task Force recommendations.
3. The generated recommendations will be displayed. Screening tests that are based only on the 
local guidelines repository will be given first; additional ones based on a search of medical literature will also be displayed.

## API Usage

The system provides a REST API for integration with other applications:

1. Start the API server: `python api.py`
2. The API will be available at http://localhost:8000
3. API endpoints:
   - POST `/api/recommendations`: You give the system a clinical note, and screening recommendations will be returned
   - GET `/api/hello`: makes sure the API is running

API documentation is available at http://localhost:8000/docs when the server is running.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
