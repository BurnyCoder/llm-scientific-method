#!/usr/bin/env python3
"""
Automate the scientific method using LLM calls.

This script implements the core steps of the scientific method:
1. Observation/Question
2. Hypothesis Formation
3. Prediction
4. Experimentation
5. Analysis & Conclusion
"""

from openai import OpenAI
import json
import os
import argparse
from dotenv import load_dotenv
from datetime import datetime

env_question = os.getenv('SCIENTIFIC_METHOD_QUESTION', "Does rapamycin increase lifespan?")

class ScientificMethod:
    def __init__(self, api_key=None, log_file=None):
        """Initialize the scientific method automation."""
        load_dotenv()
        if api_key is None:
            api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-5"
        # Generate unique log file name if not provided
        if log_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            log_file = f"scientific_method_{timestamp}.log"
        self.log_file = log_file
        self.results = {
            "question": None,
            "observations": None,
            "hypothesis": None,
            "predictions": None,
            "experiments": None,
            "experimental_data": None,
            "analysis": None,
            "conclusion": None
        }
        # Initialize log file
        with open(self.log_file, 'w') as f:
            f.write("=== Scientific Method Log ===\n\n")

    def log_and_print(self, message):
        """Print message to console and append to log file."""
        print(message)
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

    def observe(self, question):
        """
        Step 1: Define the question and gather initial observations.

        Args:
            question: The scientific question to investigate
        """
        self.results["question"] = question

        prompt = f"""You are a scientist beginning an investigation.

Question: 
{question}

Provide initial observations and context relevant to this question.
Include known facts, background information, and what we already know about this topic.
Be concise but thorough."""

        response = self.client.responses.create(
            model=self.model,
            tools=[{"type": "web_search"}],
            input=prompt
        )

        self.results["observations"] = response.output_text
        return self.results["observations"]

    def hypothesize(self):
        """
        Step 2: Form a testable hypothesis based on observations.
        """
        prompt = f"""Based on the following question and observations, formulate a clear, testable hypothesis.

Question: 
{self.results['question']}

Observations:
{self.results['observations']}

Provide a specific hypothesis that:
1. Is falsifiable
2. Makes a clear prediction
3. Can be tested through experimentation or further observation

Format your response as a single clear hypothesis statement."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        self.results["hypothesis"] = response.choices[0].message.content
        return self.results["hypothesis"]

    def predict(self):
        """
        Step 3: Generate predictions from the hypothesis.
        """
        prompt = f"""Given this hypothesis, what specific, testable predictions can we make?

Question: 
{self.results['question']}

Hypothesis: 
{self.results['hypothesis']}

Generate 3-5 specific predictions that would support or refute this hypothesis.
Each prediction should be:
1. Specific and measurable
2. Directly testable
3. Clearly linked to the hypothesis

Format as a numbered list."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        self.results["predictions"] = response.choices[0].message.content
        return self.results["predictions"]

    def experiment(self):
        """
        Step 4: Design experiments to test the predictions.
        """
        prompt = f"""Design experiments to test these predictions.

Question: 
{self.results['question']}

Hypothesis: 
{self.results['hypothesis']}

Predictions:
{self.results['predictions']}

For each prediction, describe:
1. The experimental method
2. What data to collect
3. How to control variables
4. Expected outcomes if hypothesis is correct vs. incorrect

Be specific and practical."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        self.results["experiments"] = response.choices[0].message.content
        return self.results["experiments"]

    def generate_experimental_data(self):
        """
        Step 4b: Simulate experimental data using LLM.
        """
        prompt = f"""You are conducting the following experiments. Generate realistic simulated experimental data.

Question: 
{self.results['question']}

Hypothesis: 
{self.results['hypothesis']}

Predictions:
{self.results['predictions']}

Experimental Design:
{self.results['experiments']}

Generate realistic experimental data that would result from conducting these experiments.
Include:
1. Quantitative measurements (with realistic variability)
2. Observations
3. Data tables or results summaries
4. Any unexpected findings or anomalies

Make the data realistic and internally consistent. Format it clearly."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        self.results["experimental_data"] = response.choices[0].message.content
        return self.results["experimental_data"]

    def analyze(self):
        """
        Step 5: Analyze results and draw conclusions.
        """
        experimental_data = self.results.get("experimental_data")
        if experimental_data:
            data_context = f"\nExperimental Results:\n{experimental_data}"
        else:
            data_context = "\nNote: No experimental data available. Provide theoretical analysis."

        prompt = f"""Analyze the experimental approach and draw conclusions.

Question: 
{self.results['question']}

Hypothesis: 
{self.results['hypothesis']}

Predictions:
{self.results['predictions']}

Experimental Design:
{self.results['experiments']}
{data_context}

Provide:
1. Analysis of how the experiments would test the hypothesis
2. What results would support vs. refute the hypothesis
3. Potential limitations or sources of error
4. Suggestions for follow-up investigations"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        self.results["analysis"] = response.choices[0].message.content
        return self.results["analysis"]

    def conclude(self):
        """
        Generate final conclusion based on all steps.
        """
        prompt = f"""Synthesize the entire scientific investigation into a conclusion.

Question: 
{self.results['question']}

Hypothesis: 
{self.results['hypothesis']}

Analysis: 
{self.results['analysis']}

Provide:
1. Whether the hypothesis is supported, refuted, or requires modification
2. Key findings and insights
3. Implications of the results
4. Next steps for further research

Be clear and concise."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )

        self.results["conclusion"] = response.choices[0].message.content
        return self.results["conclusion"]

    def run_full_method(self, question, generate_data=True):
        """
        Execute the complete scientific method.

        Args:
            question: The scientific question to investigate
            generate_data: Whether to generate experimental data via LLM (default: True)

        Returns:
            Dictionary containing all results
        """
        self.log_and_print(f"Question: {question}\n")

        self.log_and_print("Step 1: Gathering observations...")
        observations = self.observe(question)
        self.log_and_print(f"\n{observations}\n")
        self.log_and_print("-" * 80)

        self.log_and_print("\nStep 2: Formulating hypothesis...")
        hypothesis = self.hypothesize()
        self.log_and_print(f"\n{hypothesis}\n")
        self.log_and_print("-" * 80)

        self.log_and_print("\nStep 3: Generating predictions...")
        predictions = self.predict()
        self.log_and_print(f"\n{predictions}\n")
        self.log_and_print("-" * 80)

        self.log_and_print("\nStep 4: Designing experiments...")
        experiments = self.experiment()
        self.log_and_print(f"\n{experiments}\n")
        self.log_and_print("-" * 80)

        if generate_data:
            self.log_and_print("\nStep 4b: Generating experimental data...")
            experimental_data = self.generate_experimental_data()
            self.log_and_print(f"\n{experimental_data}\n")
            self.log_and_print("-" * 80)

        self.log_and_print("\nStep 5: Analyzing results...")
        analysis = self.analyze()
        self.log_and_print(f"\n{analysis}\n")
        self.log_and_print("-" * 80)

        self.log_and_print("\nStep 6: Drawing conclusions...")
        conclusion = self.conclude()
        self.log_and_print(f"\n{conclusion}\n")
        self.log_and_print("=" * 80)

        return self.results

    def save_results(self, filename="scientific_method_results.json"):
        """Save results to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        self.log_and_print(f"\nResults saved to {filename}")


def main():
    """Example usage of the ScientificMethod class."""
    load_dotenv()
    
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Automate the scientific method using LLM calls.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python scientific_method.py "How does photosynthesis work?"
  python scientific_method.py --question "What causes earthquakes?"
  SCIENTIFIC_METHOD_QUESTION="Why is the sky blue?" python scientific_method.py
        """
    )
    parser.add_argument(
        'question',
        nargs='?',
        help='The scientific question to investigate'
    )
    parser.add_argument(
        '--question', '-q',
        dest='question_flag',
        help='The scientific question to investigate (alternative flag form)'
    )
    parser.add_argument(
        '--no-data',
        action='store_false',
        dest='generate_data',
        help='Skip experimental data generation'
    )
    
    args = parser.parse_args()
    
    # Priority: command-line arg > env var > default
    question = args.question_flag or args.question or env_question
    
    if not question:
        parser.error("Question is required. Provide it as:\n"
                    "  - Command-line argument: python scientific_method.py 'Your question?'\n"
                    "  - Flag: python scientific_method.py --question 'Your question?'\n"
                    "  - Environment variable: SCIENTIFIC_METHOD_QUESTION='Your question?'")
    
    # Initialize the scientific method
    sm = ScientificMethod()

    # Run the full scientific method
    results = sm.run_full_method(question, generate_data=args.generate_data)

    # Save results
    sm.save_results()


if __name__ == "__main__":
    main()
