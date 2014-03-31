tablename = "dosite_place"
table = db.define_table(tablename,
            Field("name", notnull=True, length=64, label=T("Place Name")),
            s3db.pr_person_id(label=T("Place Contact")),
            Field("flyer", "upload",label=T("Flyer Propaganda")),
            s3_comments(),
            s3base.s3_date("start_date",label="Collection Start Date"),
            s3base.s3_date("end_date",label="Collection End Date"),
            *s3_meta_fields()
        )

def place_represent(id):
    table = db.dosite_place
    query = (table.id == id)
    record = db(query).select().first()
    if record:
        return record.name
    else:
        return "-"

place_id = S3ReusableField("place_id", db.dosite_place,
                    requires = IS_ONE_OF(db,
                                     "dosite_place.id",
                                     "%(name)s"),
                    represent = place_represent,
                    label = T("Place"),
                    ondelete = "RESTRICT")

LIST_PLACE =  T("List Drop-Off Sites")
s3.crud_strings[tablename] = Storage(
   title_create = T("Add New Place"),
   title_display = T("Place Details"),
   title_list = LIST_PLACE,
   title_update = T("Edit Place"),
   title_search = T("Search Place"),
   title_upload = T("Import Place"),
   subtitle_create = T("Add New Place"),
   subtitle_list = T("Place"),
   label_list_button = LIST_PLACE,
   label_create_button = T("Add New Place"),
   label_delete_button = T("Delete Place"),
   msg_record_created = T("Place added"),
   msg_record_modified = T("Place updated"),
   msg_record_deleted = T("Place deleted"),
   msg_list_empty = T("No Place currently registered"))