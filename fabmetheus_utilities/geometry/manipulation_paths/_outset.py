"""
Create inset.

"""

from __future__ import absolute_import
#Init has to be imported first because it has code to workaround the python bug where relative imports don't work if the module is imported as a main module.
import __init__

from fabmetheus_utilities.geometry.creation import lineation
from fabmetheus_utilities.geometry.geometry_utilities.evaluate_elements import setting
from fabmetheus_utilities.geometry.geometry_utilities import evaluate
from fabmetheus_utilities import intercircle


__author__ = 'Enrique Perez (perez_enrique@yahoo.com)'
__credits__ = 'Art of Illusion <http://www.artofillusion.org/>'
__date__ = '$Date: 2008/02/05 $'
__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'


globalExecutionOrder = 80


def getManipulatedPaths(close, elementNode, loop, prefix, sideLength):
	"Get outset path."
	derivation = OutsetDerivation(elementNode, prefix)
	return intercircle.getInsetLoopsFromVector3Loop(loop, -derivation.radius)

def getNewDerivation(elementNode, prefix, sideLength):
	'Get new derivation.'
	return OutsetDerivation(elementNode, prefix)

def processElementNode(elementNode):
	"Process the xml element."
	lineation.processElementNodeByFunction(elementNode, getManipulatedPaths)


class OutsetDerivation:
	"Class to hold outset variables."
	def __init__(self, elementNode, prefix):
		'Set defaults.'
		self.radius = evaluate.getEvaluatedFloat(2.0 * setting.getPerimeterWidth(elementNode), elementNode, prefix + 'radius')
