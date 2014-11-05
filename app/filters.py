import jinja2
import flask

blueprint = flask.Blueprint('filters', __name__)

@jinja2.contextfilter
@blueprint.app_template_filter()
def static_files(context, value):
    return "//static.dtable.dev/{}".format(value)
