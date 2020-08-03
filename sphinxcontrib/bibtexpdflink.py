# -- Added for APA style
# -- from: sphinxcontrib-bibtex/test/issue77

from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.labels.alpha import LabelStyle as AlphaLabelStyle
from pybtex.style.sorting import author_year_title


from pybtex.plugin import register_plugin
import os
from pybtex.style.template import (
    href, optional, sentence, words
)
# extensions = ['sphinxcontrib.bibtex']
# exclude_patterns = ['_build']


class ApaLabelStyle(AlphaLabelStyle):
    def format_label(self, entry):
        # import pdb; pdb.set_trace()
        # from: https://stackoverflow.com/questions/55942749/how-do-you-change-the-style-of-pybtex-references-in-sphinx
        label = entry.key
        return label

# split file path into parts
# from:
# https://www.oreilly.com/library/view/python-cookbook/0596001673/ch04s16.html
def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts

class FootApaStyle(UnsrtStyle):
    def format_web_refs(self, e):
        # based on urlbst output.web.refs
        return sentence [
            optional [ self.format_url(e) ],
            optional [ self.format_eprint(e) ],
            optional [ self.format_pubmed(e) ],
            optional [ self.format_doi(e) ],
            # adds link to PDF and to note
            optional [ self.format_pdf(e) ],
            optional [ self.format_rst(e) ],
            ]

    def format_pdf(self, entry):
        global saved_app
        pdf_dir = saved_app.config.bibtexpdflink_pdf_dir
        if pdf_dir is not None:
            srcdir = saved_app.srcdir
            html_static_path = saved_app.config["html_static_path"]
            pdf_dir_path = os.path.join(srcdir, html_static_path[0], pdf_dir)
            if not os.path.isdir(pdf_dir_path):
                print("Directory for pdf files not found: %s" % pdf_dir_path)
                sys.exit("aborting")
            pdf_name = entry.key + ".pdf"
            search_path = os.path.join(pdf_dir_path, pdf_name)
            if os.path.isfile(search_path):
                # now must generate relative path to download pdf
                docname = saved_app.env.docname
                path_parts = splitall(docname)
                dir_prefix = "../" * (len(path_parts) - 1)
                target_path = os.path.join(dir_prefix, html_static_path[0], pdf_dir, pdf_name)
                return words [
                    'PDF:',
                    href [ target_path, pdf_name ]
                ]
        return words [""]

    def format_rst(self, entry):
        # create link to rst file if present
        global saved_app
        note_dir = saved_app.config.bibtexpdflink_note_dir
        if note_dir is not None:
            srcdir = saved_app.srcdir
            note_dir_path = os.path.join(srcdir, note_dir)
            if not os.path.isdir(note_dir_path):
                print("Directory for note files not found: %s" % note_dir_path)
                sys.exit("aborting")
            rst_name = entry.key + ".rst"
            html_name = entry.key + ".html"
            search_path = os.path.join(note_dir_path, rst_name)
            if os.path.isfile(search_path):
                # check if this file is the note itself
                docname = saved_app.env.docname
                if search_path.endswith(docname + ".rst"):
                    # this file is the note itself
                    return words ["Notes:", html_name + " (this file)."]
                # not note, must generate relative path to download pdf
                path_parts = splitall(docname)
                dir_prefix = "../" * (len(path_parts) - 1)
                html_name = entry.key + ".html"
                target_path = os.path.join(dir_prefix, note_dir, html_name)
                return words [
                    'Notes:',
                    href [ target_path, html_name ]
                ]
        return words [""]


class ApaStyle(FootApaStyle):
    default_label_style = 'apa'
    default_sorting_style = 'author_year_title'



register_plugin('pybtex.style.labels', 'apa', ApaLabelStyle)
register_plugin('pybtex.style.formatting', 'apastyle', ApaStyle)
register_plugin('pybtex.style.formatting', 'footapastyle', FootApaStyle)
# register_plugin('pybtex.style.sorting','apastyle', ApaStyle)
register_plugin('pybtex.style.sorting','apastyle', author_year_title)


saved_app = None
def setup(app):
    app.add_config_value('bibtexpdflink_note_dir', None, 'html')
    app.add_config_value('bibtexpdflink_pdf_dir', None, 'html')

    # save app so can get config value and source directory for building links to PDF files
    global saved_app
    saved_app = app
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
