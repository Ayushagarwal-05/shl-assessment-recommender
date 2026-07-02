from app.state import ConversationState
from app.rules import RuleEngine
from app.comparison import ComparisonEngine

class Agent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.state_builder = ConversationState()
        self.rules = RuleEngine()
        self.comparison = ComparisonEngine()

    def chat(self, messages):
        """
        Main conversation handler.
        """

        # -----------------------------
        # Build conversation state
        # -----------------------------
        state = self.state_builder.build(messages)

        conversation = " ".join(
            m["content"]
            for m in messages
            if m["role"] == "user"
        ).lower()

        # -----------------------------
        # Rule : Prompt Injection
        # -----------------------------
        if self.rules.is_prompt_injection(conversation):
            return {
                "reply": (
                    "I can only help with recommending SHL assessments "
                    "using the available catalog."
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }
        
        # -----------------------------
        # Rule : Off-topic
        # -----------------------------
        if self.rules.is_off_topic(conversation):
            return {
                "reply": (
                    "I'm designed to help with SHL assessment recommendations. "
                    "I can't provide advice outside that scope."
                ),
                "recommendations": [],
                "end_of_conversation": False,
            }


        # -----------------------------
        # Rule 1 : Unsupported skills
        # -----------------------------
        skill = self.rules.check_unsupported_skill(conversation)

        if skill:
            products = self.retriever.search(
                "programming developer",
                top_k=5
            )

            recommendations = [
                {
                    "name": p["name"],
                    "url": p["link"],
                    "test_type": ", ".join(p["keys"]),
                }
                for p in products
            ]

            return {
                "reply": (
                    f"SHL doesn't currently provide a dedicated "
                    f"{skill.title()} assessment. "
                    "I'll recommend the closest relevant assessments."
                ),
                "recommendations": recommendations,
                "end_of_conversation": False,
            }

        # -----------------------------
        # Rule 2 : Clarification
        # -----------------------------
        if self.rules.needs_clarification(state):
            return {
                "reply": (
                    "I'd be happy to help. "
                    "What role or job family are you hiring for?"
                ),
                "recommendations": None,
                "end_of_conversation": False,
            }

        # -----------------------------
        # Build retrieval query
        # -----------------------------
        query_parts = []

        if state["role"]:
            query_parts.append(state["role"])

        if state["purpose"]:
            query_parts.append(state["purpose"])

        query_parts.extend(state["skills"])

        query = " ".join(query_parts)

        if not query.strip():
            query = conversation

        # -----------------------------
        # Retrieve products
        # -----------------------------
        products = self.retriever.search(query, top_k=5)

        recommendations = [
            {
                "name": product["name"],
                "url": product["link"],
                "test_type": ", ".join(product["keys"]),
            }
            for product in products
        ]

        # -----------------------------
        # Rule : Comparison
        # -----------------------------
        if self.rules.is_comparison(state):
            return {
                "reply": self.comparison.compare(products),
                "recommendations": recommendations,
                "end_of_conversation": False,
            }

        # -----------------------------
        # Response text
        # -----------------------------
        if self.rules.is_comparison(state):
            reply = (
                "I'll compare the requested SHL assessments. "
                "Here are the most relevant products from the catalog."
            )

        elif self.rules.is_refinement(state):
            reply = (
                "I've updated the recommendations based on your revised requirements."
            )

        else:
            reply = (
                "Based on your requirements, I recommend the following SHL assessments."
            )

        # -----------------------------
        # Final response
        # -----------------------------
        return {
            "reply": reply,
            "recommendations": recommendations,
            "end_of_conversation": self.rules.should_end(messages),
        }