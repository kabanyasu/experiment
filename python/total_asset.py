from edinet_xbrl.edinet_xbrl_parser import EdinetXbrlParser

parser = EdinetXbrlParser()

xbrl_file_path ="任意のディレクトリ"
edinet_xbrl_object = parser.parse_file(xbrl_file_path)

key = "jppfs_cor:Assets"
context_ref = "CurrentYearInstant"
current_year_assets = edinet_xbrl_object.get_data_by_context_ref(key, context_ref).get_value()
