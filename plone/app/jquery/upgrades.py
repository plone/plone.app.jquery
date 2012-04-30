from Products.CMFCore.utils import getToolByName
import logging
logger = logging.getLogger("Belimo")


class ImportProfileStep(object):
    """import of GenericSetup profile"""

    def __init__(self, name):
        self.name = name

    def __call__(self, context):
        logger.info("Start importing profile: " + self.name)
        tool = getToolByName(context, 'portal_setup')
        tool.runAllImportStepsFromProfile(self.name)
        logger.info("Stop importing profile: " + self.name)


def common_upgrade(context):
    """ Common upgrade for newer jQuery versions, just to call cookResources.
    """
    tool = getToolByName(context, 'portal_javascripts')
    tool.cookResources()
    logger.info("Cooked the JS Resouces")


step_1_initial_upgrade = ImportProfileStep(
    u'profile-plone.app.jquery:initial-upgrade')

upgrade_2_to_3 = common_upgrade
