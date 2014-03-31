def index():
    return dict()

def place_rheader(r, tabs=[]):
    if r.representation != "html":
        # RHeader is a UI facility & so skip for other formats
        return None
    if r.record is None:
        # List or Create form: rheader makes no sense here
        return None

    rheader_tabs = s3_rheader_tabs(r, tabs)

    place = r.record

    rheader = DIV(TABLE(
        TR(
            TH("%s: " % T("Name")),
            place.name,
            TH("%s: " % T("Start Date")),
            place.start_date,
            )
        ), rheader_tabs)

    return rheader

def place():
    return s3_rest_controller(rheader=place_rheader)
