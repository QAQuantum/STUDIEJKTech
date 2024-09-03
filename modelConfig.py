
from lingua import Language, LanguageDetectorBuilder
import uuid
from cryptography.fernet import Fernet
import calendar
from bson.int64 import Int64
import time
import random
import datetime


DATABASE_NAME = '********'
DATABASE_UID = "********"
DATABASE_PWD = "********"
DATABASE_HOST = "********"
DATABASE_PORT= 27017


MULTICLIENT_DATABASE_NAME = 'DBNAME'
MULTICLIENT_DATABASE_UID = "DBUID"
MULTICLIENT_DATABASE_PWD = "DBPWD"
MULTICLIENT_DATABASE_HOST = "DBHOST"
MULTICLIENT_DATABASE_PORT= "DBPORT"

CLASSDOCUMENT_TIMER = 'classTimer'
ADMINKEY_COLLAB = 'Collaboration'
ADMINKEY_ParentAIExams = 'ParentAIExams'
ADMINKEY_ParentAIinterviewtemplates = 'ParentAIinterviewtemplates'
ADMINKEY_ParentAIinterviewtemplatesSave = 'ParentAIinterviewtemplatesSave'
ADMINKEY_STUDIEWebinar = 'STUDIEWebinar'
ADMINKEY_analyticalSkills = 'analyticalSkills'
ADMINKEY_NEWS = 'bookDetails'
ADMINKEY_communicationSkills = 'communicationSkills'
ADMINKEY_designAssessment = 'designAssessment'
ADMINKEY_documentStatistics = 'documentStatistics'
ADMINKEY_documentumInsights_User = 'documentumInsights_User'
ADMINKEY_domainTopics = 'domainTopics'
ADMINKEY_examTrigger = 'examTrigger'
ADMINKEY_guidanceDetail = 'guidanceDetail'
ADMINKEY_interviewtemplates = 'interviewtemplates'
ADMINKEY_liveClass = 'liveClass'
ADMINKEY_notification = 'notification'
ADMINKEY_phdUsers = 'phdUsers'
ADMINKEY_problemSkills = 'problemSkills'
ADMINKEY_reallifeSkills = 'reallifeSkills'
ADMINKEY_subjectQuestions = 'subjectQuestions'
ADMINKEY_universityAssessments= 'universityAssessments'

JKHUGGINGFACE_TOKEN = '********'
JK_LLAMAMODEL = "meta-llama/Meta-Llama-3-8B"
JK_PAYLOADDATA = "For the purposes of this section, the following definitions apply: (1) “Physical restraint” means any behavioral or mechanical restraint, as defined in Section 1180.1 of the Health and Safety Code. (2) “Chemical restraint” means a drug that is used to control behavior and that is used in a manner not required to treat the patient’s medical conditions. (3) “Seclusion” means involuntary confinement of a person alone in a room or an area as defined in subdivision (e) of Section 1180.1 of the Health and Safety Code. (4) “Long-term health care facility” means a facility, as defined in Section 1418 of the Health and Safety Code, that is required to report to a regional center pursuant to Section 54327 of Title 17 of the California Code of Regulations. (5) “Acute psychiatric hospital” means a facility, as defined in subdivision (b) of Section 1250 of the Health and Safety Code, including an institution for mental disease, that is a regional center vendor. (6) “Regional center vendor” means an agency, individual, or service provider that a regional center has approved to provide vendored or contracted services or supports pursuant to paragraph (3) of subdivision (a) of Section 4648. (b) All regional center vendors that provide residential services or supported living services, long-term health care facilities, and acute psychiatric hospitals shall report each death or serious injury of a person occurring during, or related to, the use of seclusion, physical restraint, or chemical restraint, or any combination thereof, to the agency designated pursuant to subdivision (i) of Section 4900 no later than the close of the business day following the death or serious injury. The report shall include the encrypted identifier of the person involved, and the name, street address, and telephone number of the facility.\" A key of the example: \"summary\" The value corresponding to the key-\"summary\" \"Existing law requires the Secretary of California Health and Human Services to develop technical assistance and training programs to support the efforts of community care facilities, group homes, skilled nursing facilities, intermediate care facilities, and mental health rehabilitation centers, among others, to reduce or eliminate the use of seclusion and behavioral restraints in these facilities. Existing law requires specified entities within the California Health and Human Services Agency to take steps to establish a system of mandatory, consistent, timely, and publicly accessible data collection regarding the use of seclusion and behavioral restraints in state hospitals operated by the State Department of State Hospitals, facilities operated by the State Department of Developmental Services, and other specified facilities that utilize seclusion or behavioral restraints. Under existing law, the Lanterman Developmental Disabilities Services Act, the State Department of Developmental Services contracts with regional centers to provide services and supports to individuals with developmental disabilities. Existing law requires all vendors and long-term health care facilities, as defined, to report special incidents to a regional center, including, among other things, incidents of physical and chemical restraint. Existing law requires a regional center that receives information from a special incident report regarding the use of physical or chemical restraint, to report that information to the department, as specified. This bill would require the department to ensure the consistent, timely, and public reporting of data it receives from regional centers and other specified facilities regarding the use of physical or chemical restraint and to publish that information on its Internet Web site. This bill would also require regional center vendors that provide residential services or supported living services, long-term health care facilities, as defined, and acute psychiatric hospitals, as defined, to report each death or serious injury of a person occurring during, or related to, the use of seclusion, physical restraint, or chemical restraint, as specified. This bill would make related findings and declarations.\" A key of the example: \"title\" The value corresponding to the key-\"title\"  \"An act to add Sections 4436.5 and 4659.2 to the Welfare and Institutions Code, relating to seclusion and restraint."
JK_PIPELINE_SUMMARIZATION = "summarization"
COLL_JK = 'sampleJKCollection'