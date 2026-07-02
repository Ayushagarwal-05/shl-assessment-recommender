class ComparisonEngine:

    def compare(self, products):

        if len(products) < 2:
            return "I couldn't find enough SHL assessments to compare."

        p1 = products[0]
        p2 = products[1]

        return f"""
Comparison of SHL Assessments

1. {p1['name']}
   • Test Type : {", ".join(p1.get("keys", []))}
   • Duration  : {p1.get("duration", "N/A")}
   • Remote    : {p1.get("remote", "Unknown")}
   • Adaptive  : {p1.get("adaptive", "Unknown")}

2. {p2['name']}
   • Test Type : {", ".join(p2.get("keys", []))}
   • Duration  : {p2.get("duration", "N/A")}
   • Remote    : {p2.get("remote", "Unknown")}
   • Adaptive  : {p2.get("adaptive", "Unknown")}
"""