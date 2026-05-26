from xml.dom import minidom
from xml.sax import make_parser, handler
from datetime import datetime

XML_FILE = "go_obo.xml"
ONTOLOGIES = [
    "molecular_function",
    "biological_process",
    "cellular_component"
]

def empty_results():
    results = {}
    for ontology in ONTOLOGIES:
        results[ontology] = {
            "id": "",
            "name": "",
            "is_a_count": -1
        }

    return results

def get_text(parent, tag):
    elements = parent.getElementsByTagName(tag)

    if not elements:
        return ""
    if elements[0].firstChild is None:
        return ""

    return elements[0].firstChild.data.strip()

def analyse_with_dom(filename):
    results = empty_results()
    doc = minidom.parse( str(filename) )
    terms = doc.getElementsByTagName("term")

    for term in terms:
        go_id = get_text(term, "id")
        name = get_text(term, "name")
        namespace = get_text(term, "namespace")

        if namespace in results:
            is_a_count = len(term.getElementsByTagName("is_a"))

            if is_a_count > results[namespace]["is_a_count"]:
                results[namespace] = {
                    "id": go_id,
                    "name": name,
                    "is_a_count": is_a_count
                }

    return results


class GOHandler(handler.ContentHandler):
    def __init__(self):
        self.results = empty_results()

        self.in_term = False
        self.current_tag = ""

        self.go_id = ""
        self.name = ""
        self.namespace = ""
        self.is_a_count = 0

    def startElement(self, name, attrs):
        self.current_tag = name

        if name == "term":
            self.in_term = True
            self.go_id = ""
            self.name = ""
            self.namespace = ""
            self.is_a_count = 0
        elif self.in_term and name == "is_a":
            self.is_a_count += 1

    def characters(self, content):
        if not self.in_term:
            return

        if self.current_tag == "id":
            self.go_id += content.strip()
        elif self.current_tag == "name":
            self.name += content.strip()
        elif self.current_tag == "namespace":
            self.namespace += content.strip()

    def endElement(self, name):
        if name == "term":
            if self.namespace in self.results:
                old_count = self.results[self.namespace]["is_a_count"]

                if self.is_a_count > old_count:
                    self.results[self.namespace] = {
                        "id": self.go_id,
                        "name": self.name,
                        "is_a_count": self.is_a_count
                    }
            self.in_term = False

        self.current_tag = ""


def analyse_with_sax(filename):
    parser = make_parser()
    go_handler = GOHandler()

    parser.setContentHandler(go_handler)
    parser.parse(filename)

    return go_handler.results


def print_results(title, results):
    print(title)
    print("-" * 60)

    for ontology in ONTOLOGIES:
        result = results[ontology]

        print(f"Ontology: {ontology}")
        print(f"GO ID: {result['id']}")
        print(f"Name: {result['name']}")
        print(f"Number of is_a elements: {result['is_a_count']}")
        print()

    print()


start_dom = datetime.now()
dom_results = analyse_with_dom(XML_FILE)
end_dom = datetime.now()

dom_time = (end_dom - start_dom).total_seconds()


start_sax = datetime.now()
sax_results = analyse_with_sax(XML_FILE)
end_sax = datetime.now()

sax_time = (end_sax - start_sax).total_seconds()


print_results("DOM results", dom_results)
print_results("SAX results", sax_results)

print("Time taken")
print("-" * 60)
print(f"DOM time: {dom_time:.4f} seconds")
print(f"SAX time: {sax_time:.4f} seconds")

if dom_time < sax_time:
    print("DOM was faster in this run.")
    # Fastest API in this run: DOM
elif sax_time < dom_time:
    print("SAX was faster in this run.")
    # Fastest API in this run: SAX
else:
    print("DOM and SAX took the same time in this run.")
    # Fastest API in this run: equal time

# comment: In my run, SAX was faster than DOM.