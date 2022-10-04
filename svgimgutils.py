import random
import string

import cssutils
from lxml import etree

SVG_NAMESPACE = "http://www.w3.org/2000/svg"
XLINK_NAMESPACE = "http://www.w3.org/1999/xlink"
SVG = "{%s}" % SVG_NAMESPACE
XLINK = "{%s}" % XLINK_NAMESPACE
NSMAP = {None: SVG_NAMESPACE,
         'xlink': XLINK_NAMESPACE}


class FigureElement(object):
    """Base class representing single figure element"""
    def __init__(self, xml_element, defs=None):

        self.root = xml_element


class GroupElement(FigureElement):
    """Group element.

    Container for other elements. Corresponds to SVG ``<g>`` tag.
    """
    def __init__(self, element_list, attrib=None):
        new_group = etree.Element(SVG+"g", attrib=attrib)
        for e in element_list:
            if isinstance(e, FigureElement):
                new_group.append(e.root)
            else:
                new_group.append(e)
        self.root = new_group


class SVGImgUtils(object):

    def __init__(self):
        self.root = etree.Element(SVG + "svg", nsmap=NSMAP)
        self.root.set("version", "1.1")
        self.prepend = ''.join(random.choice(string.ascii_uppercase) for _ in range(6))

    def append(self, element):
        """Append new element to the svgimgutils

                Parameters
                ----------
                element : SVGImgUtils
                    an SVG element to append

                """
        try:
            self.root.append(element.root)
        except AttributeError:
            self.root.append(GroupElement(element).root)

    def getroot(self):
        """Return the root element of the utils.

        The root element is a group of elements after stripping the toplevel
        ``<svg>`` tag.

        Returns
        -------
        GroupElement
            All elements of the figure without the ``<svg>`` tag.
        """
        if 'class' in self.root.attrib:
            attrib = {'class': self.root.attrib['class']}
        else:
            attrib = None
        return GroupElement(self.root.getchildren(), attrib=attrib)

    def to_str(self):
        """
        Returns a string of the svgimgutils.
        """
        return etree.tostring(self.root, xml_declaration=True,
                              standalone=True,
                 pretty_print=True)

    def save(self, fname):
        """Save SVG to a file"""
        out = etree.tostring(self.root, xml_declaration=True,
                             standalone=True,
                             pretty_print=True)
        fid = open(fname, 'wb')
        fid.write(out)
        fid.close()

    def fromfile(fname):
        """Create a SVGImgUtils from file.

        Parameters
        ----------
        fname : str
            path to the name of the SVG file

        Returns
        -------
        SVGImgUtils
            newly created :py:class:`SVGImgUtils` initialised with the file content
        """
        fig = SVGImgUtils()
        fid = open(fname)
        svg_file = etree.parse(fid)
        fid.close()
        fig.root = svg_file.getroot()
        fig.setup()
        return fig

    def fromstring(text):
        """Create a SVGImgUtils from a string.

        Parameters
        ----------
        text : str
            string representing the SVG content. Must be valid SVG.

        Returns
        -------
        SVGImgUtils
            newly created :py:class:`SVGImgUtils` initialised with the string
            content.
        """
        fig = SVGImgUtils()
        svg = etree.fromstring(text.encode())

        fig.root = svg
        fig.setup()

        return fig

    # ----PRIVATE METHODS----

    def setup(self):
        self.adddata()
        self.makemodifications()

    def adddata(self):
        """Add more data to the svgimgutils"""
        if len(self.root[0]):
            self.style_element = self.root.find('./' + self.root[0].tag + '/' + self.root[0][0].tag)
        else:
            self.style_element = self.root.find('./' + self.root[0].tag)
        self.number_of_classes = cssutils.parseString(self.style_element.text).cssRules.length

    def makemodifications(self):
        group_elements = self.root.findall('.')
        for g in group_elements:
            self.modifygroupvalues(g)
        # Change the style tag according to the number of classes in the SVG
        self.style_element.text = self.modifystylevalues(self.style_element.text)

    def modifygroupvalues(self, group_element):
        """
        Change cls-x value to a number aligned with total number of classes in the svgimgutils
        Parameters
        ----------
        group_element : _Element
            XML Element that its and its children cls-x value should change
        """
        for c in group_element.iter():
            cls = c.attrib.get('class')
            if cls is not None:
                c.attrib['class'] = f"{self.prepend}-{cls}"
                

    def modifystylevalues(self,css_string):
        """
        Change cls-x selectors to a number aligned with total number of classes in the svgimgutils
        Parameters
        ----------
        css_string : str
            A css formed string. Its cls-x selectors should change.

        Returns
        -------
        str
            A modified css style string.
        """
        sheet = cssutils.parseString(css_string)
        for rule in sheet:
            # If there are a couple of classes in one selectorText
            if ',' in rule.selectorText:
                classes_selectors = rule.selectorText.split(',')
                selectors = ''
                for selectorText in classes_selectors:
                    cls = selectorText
                    selectors += f"&{self.prepend}-{cls}"
                    
                # '&' is used as a place holder for ','. Replace them and discard the first ','
                rule.selectorText = selectors.replace('&', ',')[1:]

            else:
                cls_type = rule.selectorText[0]
                cls = rule.selectorText[1:]
                rule.selectorText = f"{cls_type}{self.prepend}-{cls}"

        css_without_newline_chars = str(sheet.cssText)[2:].replace('\\n', '')
        translator = str.maketrans('', '', ' \t\r')
        return css_without_newline_chars.translate(translator)
