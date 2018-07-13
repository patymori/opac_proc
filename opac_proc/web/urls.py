# coding: utf-8
from flask_login import login_required
from opac_proc.web.views.extract.list_views import (
    ExtractCollectionListView,
    ExtractJournalListView,
    ExtractIssueListView,
    ExtractArticleListView,
    ExtractPressReleaseListView,
    ExtractNewsListView,
    ExtractLogListView)

from opac_proc.web.views.extract.detail_views import (
    ExtractCollectionDetailView,
    ExtractJournalDetailView,
    ExtractIssueDetailView,
    ExtractArticleDetailView,
    ExtractPressReleaseDetailView,
    ExtractNewsDetailView,
    ExtractLogDetailView)

from opac_proc.web.views.transform.list_views import (
    TransformCollectionListView,
    TransformJournalListView,
    TransformIssueListView,
    TransformArticleListView,
    TransformPressReleaseListView,
    TransformNewsListView,
    TransformLogListView)

from opac_proc.web.views.transform.detail_views import (
    TransformCollectionDetailView,
    TransformJournalDetailView,
    TransformIssueDetailView,
    TransformArticleDetailView,
    TransformPressReleaseDetailView,
    TransformNewsDetailView,
    TransformLogDetailView)

from opac_proc.web.views.load.list_views import (
    LoadCollectionListView,
    LoadJournalListView,
    LoadIssueListView,
    LoadArticleListView,
    LoadPressReleaseListView,
    LoadNewsListView,
    LoadLogListView)

from opac_proc.web.views.load.detail_views import (
    LoadCollectionDetailView,
    LoadJournalDetailView,
    LoadIssueDetailView,
    LoadArticleDetailView,
    LoadPressReleaseDetailView,
    LoadNewsDetailView,
    LoadLogDetailView)

from opac_proc.web.views.opac.list_views import (
    OpacCollectionListView,
    OpacJournalListView,
    OpacIssueListView,
    OpacArticleListView,
    OpacSponsorListView,
    OpacPageListView,
    OpacPressReleaseListView,
    OpacNewsListView)

from opac_proc.web.views.opac.detail_views import (
    OpacCollectionDetailView,
    OpacJournalDetailView,
    OpacIssueDetailView,
    OpacArticleDetailView,
    OpacSponsorDetailView,
    OpacPageDetailView,
    OpacPressReleaseDetailView,
    OpacNewsDetailView)

from opac_proc.web.views.source_sync.list_views import (
    IdentifiersCollectionListView,
    IdentifiersJournalListView,
    IdentifiersIssueListView,
    IdentifiersArticleListView,
    IdentifiersPressReleaseListView,
    IdentifiersNewsListView)

from opac_proc.web.views.source_sync.detail_views import (
    IdentifiersCollectionDetailView,
    IdentifiersJournalDetailView,
    IdentifiersIssueDetailView,
    IdentifiersArticleDetailView,
    IdentifiersPressReleaseDetailView,
    IdentifiersNewsDetailView)


from opac_proc.web.views.message.list_views import (
    MessageListView)

from opac_proc.web.views.message.detail_views import (
    MessageDetailView)

from opac_proc.web.views.home import home, download_file_by_filename
from opac_proc.web.views.export_report import export_failed_jobs
from opac_proc.web.views.source_sync.timeline import timeline_index

url_patterns = (
    {
        'stage': 'extract',
        'models': {
            'collection': {
                'list_view_class': ExtractCollectionListView,
                'detail_view_class': ExtractCollectionDetailView,
            },
            'journal': {
                'list_view_class': ExtractJournalListView,
                'detail_view_class': ExtractJournalDetailView,
            },
            'issue': {
                'list_view_class': ExtractIssueListView,
                'detail_view_class': ExtractIssueDetailView,
            },
            'article': {
                'list_view_class': ExtractArticleListView,
                'detail_view_class': ExtractArticleDetailView,
            },
            'press_release': {
                'list_view_class': ExtractPressReleaseListView,
                'detail_view_class': ExtractPressReleaseDetailView,
            },
            'news': {
                'list_view_class': ExtractNewsListView,
                'detail_view_class': ExtractNewsDetailView,
            },
            'logs': {
                'list_view_class': ExtractLogListView,
                'detail_view_class': ExtractLogDetailView,
            }
        }
    },
    {
        'stage': 'transform',
        'models': {
            'collection': {
                'list_view_class': TransformCollectionListView,
                'detail_view_class': TransformCollectionDetailView,
            },
            'journal': {
                'list_view_class': TransformJournalListView,
                'detail_view_class': TransformJournalDetailView,
            },
            'issue': {
                'list_view_class': TransformIssueListView,
                'detail_view_class': TransformIssueDetailView,
            },
            'article': {
                'list_view_class': TransformArticleListView,
                'detail_view_class': TransformArticleDetailView,
            },
            'press_release': {
                'list_view_class': TransformPressReleaseListView,
                'detail_view_class': TransformPressReleaseDetailView,
            },
            'news': {
                'list_view_class': TransformNewsListView,
                'detail_view_class': TransformNewsDetailView,
            },
            'logs': {
                'list_view_class': TransformLogListView,
                'detail_view_class': TransformLogDetailView,
            }
        }
    },
    {
        'stage': 'load',
        'models': {
            'collection': {
                'list_view_class': LoadCollectionListView,
                'detail_view_class': LoadCollectionDetailView,
            },
            'journal': {
                'list_view_class': LoadJournalListView,
                'detail_view_class': LoadJournalDetailView,
            },
            'issue': {
                'list_view_class': LoadIssueListView,
                'detail_view_class': LoadIssueDetailView,
            },
            'article': {
                'list_view_class': LoadArticleListView,
                'detail_view_class': LoadArticleDetailView,
            },
            'press_release': {
                'list_view_class': LoadPressReleaseListView,
                'detail_view_class': LoadPressReleaseDetailView,
            },
            'news': {
                'list_view_class': LoadNewsListView,
                'detail_view_class': LoadNewsDetailView,
            },
            'logs': {
                'list_view_class': LoadLogListView,
                'detail_view_class': LoadLogDetailView,
            }
        }
    },
    {
        'stage': 'opac',
        'models': {
            'collection': {
                'list_view_class': OpacCollectionListView,
                'detail_view_class': OpacCollectionDetailView,
            },
            'journal': {
                'list_view_class': OpacJournalListView,
                'detail_view_class': OpacJournalDetailView,
            },
            'issue': {
                'list_view_class': OpacIssueListView,
                'detail_view_class': OpacIssueDetailView,
            },
            'article': {
                'list_view_class': OpacArticleListView,
                'detail_view_class': OpacArticleDetailView,
            },
            'sponsor': {
                'list_view_class': OpacSponsorListView,
                'detail_view_class': OpacSponsorDetailView,
            },
            'page': {
                'list_view_class': OpacPageListView,
                'detail_view_class': OpacPageDetailView,
            },
            'pressrelease': {
                'list_view_class': OpacPressReleaseListView,
                'detail_view_class': OpacPressReleaseDetailView,
            },
            'news': {
                'list_view_class': OpacNewsListView,
                'detail_view_class': OpacNewsDetailView,
            }
        }
    },
    {
        'stage': 'default',
        'models': {
            'message': {
                'list_view_class': MessageListView,
                'detail_view_class': MessageDetailView,
            }
        }
    },
    {
        'stage': 'sync_ids',
        'models': {
            'collection': {
                'list_view_class': IdentifiersCollectionListView,
                'detail_view_class': IdentifiersCollectionDetailView,
            },
            'journal': {
                'list_view_class': IdentifiersJournalListView,
                'detail_view_class': IdentifiersJournalDetailView,
            },
            'issue': {
                'list_view_class': IdentifiersIssueListView,
                'detail_view_class': IdentifiersIssueDetailView,
            },
            'article': {
                'list_view_class': IdentifiersArticleListView,
                'detail_view_class': IdentifiersArticleDetailView,
            },
            'press_release': {
                'list_view_class': IdentifiersPressReleaseListView,
                'detail_view_class': IdentifiersPressReleaseDetailView,
            },
            'news': {
                'list_view_class': IdentifiersNewsListView,
                'detail_view_class': IdentifiersNewsDetailView,
            },
        }
    },
)


def add_url_rules(app):
    # first add home page:
    app.add_url_rule('/', 'home', login_required(home))
    app.add_url_rule('/timeline/', 'timeline', login_required(timeline_index))
    app.add_url_rule('/export/failed', 'export_failed_jobs', login_required(export_failed_jobs))
    app.add_url_rule('/static_pdf_files.txt',
                     view_func=download_file_by_filename)
    app.add_url_rule('/static_html_files.txt',
                     view_func=download_file_by_filename)
    app.add_url_rule('/static_xml_files.txt',
                     view_func=download_file_by_filename)

    # then iterate over url_patterns to add each view:
    for url_definition in url_patterns:
        stage = url_definition['stage']
        models_data = url_definition['models']

        for model_name, view_classes in models_data.iteritems():

            list_view_class = view_classes['list_view_class']
            detail_view_class = view_classes['detail_view_class']

            list_view_name = "%s.%s_list" % (stage, model_name)
            detail_view_name = "%s.%s_detail" % (stage, model_name)

            list_url_path = "/%s/%s/" % (stage, model_name)
            detail_url_path = "/%s/%s/<string:object_id>/" % (stage, model_name)

            # add list rule
            app.add_url_rule(
                list_url_path,
                view_func=login_required(
                    list_view_class.as_view(list_view_name)
                )
            )

            # add detail rule
            app.add_url_rule(
                detail_url_path,
                view_func=login_required(
                    detail_view_class.as_view(detail_view_name)
                )
            )
