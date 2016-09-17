# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LayerStyleLoader
                                 A QGIS plugin
 Load multiple layer styles based on layer names
                             -------------------
        begin                : 2016-09-16
        copyright            : (C) 2016 by Bernd Loigge
        email                : bernd.loigge@gmx.at
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LayerStyleLoader class from file LayerStyleLoader.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .layer_style_loader import LayerStyleLoader
    return LayerStyleLoader(iface)
