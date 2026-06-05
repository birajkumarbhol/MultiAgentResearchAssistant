
from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.researcher import ResearchAgent
from agents.memory_agent import MemoryAgent
from agents.analyst import AnalystAgent
from agents.writer import WriterAgent


def main():
    planner = PlannerAgent()
    search_agent = SearchAgent()
    researcher = ResearchAgent()
    memory_agent = MemoryAgent()
    analyst = AnalystAgent()
    writer = WriterAgent()

    query = "Research the AI startup market in India"

    print("\nSTEP 1: Creating Research Plan...\n")
    plan = planner.create_plan(query)
    print(plan)

    print("\nSTEP 2: Running Search Agent...\n")

    first_task = plan.split("\n")[0]
    search_results = search_agent.search_topic(first_task)

    for idx, result in enumerate(search_results, 1):
        print(f"Result {idx}")
        print(f"Title: {result['title']}")
        print(f"Link: {result['link']}")
        print(f"Snippet: {result['snippet']}")
        print("-" * 50)

    print("\nSTEP 3: Running Research Agent...\n")

    research_analysis = researcher.analyze_search_results(
        query=first_task,
        search_results=search_results
    )

    print(research_analysis)

    print("\nSTEP 4: Running Analyst Agent...\n")

    business_analysis = analyst.analyze(research_analysis)
    print(business_analysis)

    print("\nSTEP 5: Running Writer Agent...\n")

    final_report = writer.write_report(business_analysis)
    print(final_report)

    print("\nSTEP 6: Saving Final Report to Memory...\n")

    memory_agent.save_memory(
        query=query,
        analysis=final_report
    )

    print("Final professional report saved successfully.")

    print("\nSTEP 7: Loading Previous Memory...\n")

    previous_memory = memory_agent.load_memory()

    for idx, item in enumerate(previous_memory, 1):
        print(f"Memory {idx}")
        print(f"Query: {item['query']}")
        print(f"Analysis: {item['analysis']}")
        print("-" * 50)


if __name__ == "__main__":
    main()
