#takes a file directory of .json FHIR patients and parses them
import json
import os
from fhir.resources.patient import Patient
from fhir.resources.bundle import Bundle
from fhir.resources.condition import Condition
from fhir.resources.resource import Resource


def parse_patient(patient_fhir_file) -> Patient:
    #takes one patient .json file and returns a validated FHIR Patient resource
    #args: patient_fhir_file (str): path to patient.json file
    #returns: a validated FHIR Patient

    with open(patient_fhir_file) as f:
        try:
            raw_data = json.load(f)
            if raw_data.get("resourceType") != 'Bundle':
                raise ValueError(f"Expected resourceType 'Bundle', got '{raw_data.get('resourceType')}'")
            for entry_item in raw_data.get("entry"):
                if entry_item.get("resource").get("resourceType") == 'Patient':
                    
                    raise ValueError(f"Expected resourceType 'Patient', got '{entry_item.get('resource').get('resourceType')}'")
            
            for entryitem in bundle.entry:
                print(f"found resource: {entryitem.resource}")
            # print(f"Patient: {patient}")
        except FileNotFoundError:
            print(f"File not found")
            return None
        except json.JSONDecodeError as je:
            print(f"json decode error: {je}")
            return None
        except ValueError as ve:  
            print(f"Unexpected FHIR structure in {patient_fhir_file}: {ve}")
            return None
        except Exception as e:
            print(f"Unexpected Error: {e}")
            return None
    

def parse_all_patients():
    #takes a directory of patient.json files and returns a list of validated FHIR Patient resources
    #args: patient_fhir_file (str): path to patient directory
    #returns: a list of validated FHIR Patients
    patients = []
    current_file = os.path.abspath(__file__)
    project_root = os.path.abspath(os.path.join(os.path.dirname(current_file),'../'))
    patient_data_path = os.path.join(project_root, 'patient_data')
    try:
        for patient_filename in os.listdir(patient_data_path):
            if patient_filename.endswith(".json"):
                full_patient_filepath = os.path.join(patient_data_path, patient_filename)
            patients.append(parse_patient(full_patient_filepath))
        print(f"{len(patients)} loaded: {patients}")
    except NotADirectoryError as e:
        print(f"Could not find directory error: {e}")
    except Exception as e:
        print(f"Unexpected error loading all patients: {e}")