import requests

# !! be sure to keep this up to date after regenerating !!

from .api.assessment_types import AssessmentTypesApiModule
from .api.assessments import AssessmentsApiModule
from .api.asset_types import AssetTypesApiModule
from .api.assets import AssetsApiModule
from .api.auth import AuthApiModule
from .api.checklist_result_lines import ChecklistResultLinesApiModule
from .api.checklist_tasks import ChecklistTasksApiModule
from .api.checklist_templates_fillable import ChecklistTemplatesFillableApiModule
from .api.checklist_templates import ChecklistTemplatesApiModule
from .api.checklists import ChecklistsApiModule
from .api.cmls import CmlsApiModule
from .api.companies import CompaniesApiModule
from .api.crews import CrewsApiModule
from .api.defect_profiles import DefectProfilesApiModule
from .api.defects import DefectsApiModule
from .api.heat_data import HeatDataApiModule
from .api.inspection_media_overlays import InspectionMediaOverlaysApiModule
from .api.inspection_media import InspectionMediaApiModule
from .api.libraries import LibrariesApiModule
from .api.library_media import LibraryMediaApiModule
from .api.location_layer_profiles import LocationLayerProfilesApiModule
from .api.measurements import MeasurementsApiModule
from .api.observations_summary import ObservationsSummaryApiModule
from .api.pages import PagesApiModule
from .api.project_types import ProjectTypesApiModule
from .api.projects import ProjectsApiModule
from .api.recommended_work_plans import RecommendedWorkPlansApiModule
from .api.reservations import ReservationsApiModule
from .api.schedules import SchedulesApiModule
from .api.users import UsersApiModule


class HuvrClient:
    """
    REST API for HUVR.

    See full REST API documentation at https://docs.huvrdata.com
    """

    def __init__(
        self,
        base_url: str,
        verbose: bool = False,
    ):
        """
        Initialize the client.

        :param base_url: The base URL for the HUVR API. ex: https://demo.huvrdata.com
        :param verbose: print debug to stdout.
        """
        self.base_url = base_url
        # remove trailing slash if present
        if self.base_url.endswith("/"):
            self.base_url = self.base_url[:-1]

        self.verbose = verbose
        self.session = requests.Session()

        # modules
        #
        self.assessment_types = AssessmentTypesApiModule(self)
        self.assessments = AssessmentsApiModule(self)
        self.asset_types = AssetTypesApiModule(self)
        self.assets = AssetsApiModule(self)
        self.auth = AuthApiModule(self)
        self.checklist_result_lines = ChecklistResultLinesApiModule(self)
        self.checklist_tasks = ChecklistTasksApiModule(self)
        self.checklist_templates_fillable = ChecklistTemplatesFillableApiModule(self)
        self.checklist_templates = ChecklistTemplatesApiModule(self)
        self.checklists = ChecklistsApiModule(self)
        self.cmls = CmlsApiModule(self)
        self.companies = CompaniesApiModule(self)
        self.crews = CrewsApiModule(self)
        self.defect_profiles = DefectProfilesApiModule(self)
        self.defects = DefectsApiModule(self)
        self.heat_data = HeatDataApiModule(self)
        self.inspection_media_overlays = InspectionMediaOverlaysApiModule(self)
        self.inspection_media = InspectionMediaApiModule(self)
        self.libraries = LibrariesApiModule(self)
        self.library_media = LibraryMediaApiModule(self)
        self.location_layer_profiles = LocationLayerProfilesApiModule(self)
        self.measurements = MeasurementsApiModule(self)
        self.observations_summary = ObservationsSummaryApiModule(self)
        self.pages = PagesApiModule(self)
        self.project_types = ProjectTypesApiModule(self)
        self.projects = ProjectsApiModule(self)
        self.recommended_work_plans = RecommendedWorkPlansApiModule(self)
        self.reservations = ReservationsApiModule(self)
        self.schedules = SchedulesApiModule(self)
        self.users = UsersApiModule(self)

    def request(self, method: str, path: str, **kwargs) -> "requests.Response":
        url = self.base_url + path

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            **kwargs.pop("headers", {}),
        }

        if self.verbose:
            print(
                "HUVR HTTP REQUEST: {} {} {}".format(
                    method,
                    url,
                    {
                        "headers": headers,
                        **kwargs,
                    },
                )
            )

        return self.session.request(
            method,
            url,
            headers=headers,
            **kwargs,
        )

    def authenticate(self, client_id: str, client_secret: str):
        """
        Authenticate with the HUVR API.

        The access token is good for 60 minutes.  Then must re-authenticate.

        https://docs.huvrdata.app/docs/authentication
        """
        response = self.auth.obtain_access_token_create(
            json={
                "client_id": client_id,
                "client_secret": client_secret,
            }
        )
        response.raise_for_status()
        data = response.json()
        self.session.headers["Authorization"] = f"Token {data['access_token']}"


def get_huvr_client(base_url: str, client_id: str = None, client_secret: str = None) -> "HuvrClient":
    """
    Get an authenticated HUVR client.

    :param base_url: The base URL for the HUVR API. ex: https://demo.huvrdata.com
    :param client_id: The client ID for the HUVR API.
        optional - if passed will authenticate the client.
    :param client_secret: The client secret for the HUVR API.
        optional - must include client_id if passed.
    :return: An authenticated HUVR client.
    """
    client = HuvrClient(base_url)
    if client_id:
        client.authenticate(client_id, client_secret)
    return client
