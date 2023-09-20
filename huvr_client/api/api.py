from .assessment_types import AssessmentTypesApiModule

from .assessments import AssessmentsApiModule

from .asset_types import AssetTypesApiModule

from .assets import AssetsApiModule

from .auth import AuthApiModule

from .checklist_result_lines import ChecklistResultLinesApiModule

from .checklist_tasks import ChecklistTasksApiModule

from .checklist_templates_fillable import ChecklistTemplatesFillableApiModule

from .checklist_templates import ChecklistTemplatesApiModule

from .checklists import ChecklistsApiModule

from .cmls import CmlsApiModule

from .companies import CompaniesApiModule

from .crews import CrewsApiModule

from .defect_profiles import DefectProfilesApiModule

from .defects import DefectsApiModule

from .heat_data import HeatDataApiModule

from .inspection_media_overlays import InspectionMediaOverlaysApiModule

from .inspection_media import InspectionMediaApiModule

from .libraries import LibrariesApiModule

from .library_media import LibraryMediaApiModule

from .location_layer_profiles import LocationLayerProfilesApiModule

from .measurements import MeasurementsApiModule

from .observations_summary import ObservationsSummaryApiModule

from .pages import PagesApiModule

from .project_types import ProjectTypesApiModule

from .projects import ProjectsApiModule

from .recommended_work_plans import RecommendedWorkPlansApiModule

from .reservations import ReservationsApiModule

from .schedules import SchedulesApiModule

from .users import UsersApiModule


class Api:
    def __init__(self, client):
        self.assessment_types = AssessmentTypesApiModule(client)

        self.assessments = AssessmentsApiModule(client)

        self.asset_types = AssetTypesApiModule(client)

        self.assets = AssetsApiModule(client)

        self.auth = AuthApiModule(client)

        self.checklist_result_lines = ChecklistResultLinesApiModule(client)

        self.checklist_tasks = ChecklistTasksApiModule(client)

        self.checklist_templates_fillable = ChecklistTemplatesFillableApiModule(client)

        self.checklist_templates = ChecklistTemplatesApiModule(client)

        self.checklists = ChecklistsApiModule(client)

        self.cmls = CmlsApiModule(client)

        self.companies = CompaniesApiModule(client)

        self.crews = CrewsApiModule(client)

        self.defect_profiles = DefectProfilesApiModule(client)

        self.defects = DefectsApiModule(client)

        self.heat_data = HeatDataApiModule(client)

        self.inspection_media_overlays = InspectionMediaOverlaysApiModule(client)

        self.inspection_media = InspectionMediaApiModule(client)

        self.libraries = LibrariesApiModule(client)

        self.library_media = LibraryMediaApiModule(client)

        self.location_layer_profiles = LocationLayerProfilesApiModule(client)

        self.measurements = MeasurementsApiModule(client)

        self.observations_summary = ObservationsSummaryApiModule(client)

        self.pages = PagesApiModule(client)

        self.project_types = ProjectTypesApiModule(client)

        self.projects = ProjectsApiModule(client)

        self.recommended_work_plans = RecommendedWorkPlansApiModule(client)

        self.reservations = ReservationsApiModule(client)

        self.schedules = SchedulesApiModule(client)

        self.users = UsersApiModule(client)
