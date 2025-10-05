# Scientific Method Automation

Automate the scientific method using LLM calls. This Python script implements the core steps of the scientific method through AI-powered analysis and reasoning.

## Overview

This tool guides you through a complete scientific investigation by:

1. **Observation/Question** - Gathering initial observations and context
2. **Hypothesis Formation** - Creating testable hypotheses
3. **Prediction** - Generating specific, measurable predictions
4. **Experimentation** - Designing experiments to test predictions
5. **Analysis** - Analyzing experimental approaches and results
6. **Conclusion** - Synthesizing findings and suggesting next steps

## Features

- 🔬 **Complete Scientific Method Pipeline** - Automated workflow through all scientific method steps
- 🌐 **Web Search Integration** - Uses web search for gathering observations and context
- 📊 **Experimental Data Generation** - Can simulate realistic experimental data
- 📝 **Comprehensive Logging** - Saves detailed logs with timestamps
- 💾 **JSON Export** - Results saved in structured JSON format
- 🎯 **Flexible Input** - Multiple ways to specify research questions

## Requirements

- Python 3.7+
- OpenAI API key with access to GPT-5 (or modify `self.model` in code for other models)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/scientific-method.git
cd scientific-method
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your OpenAI API key:
```bash
# Create a .env file
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

## Usage

### Basic Usage

```bash
# Provide question as command-line argument
python scientific_method.py "Does rapamycin increase lifespan?"

# Use the --question flag
python scientific_method.py --question "How does photosynthesis work?"

# Set via environment variable
SCIENTIFIC_METHOD_QUESTION="What causes earthquakes?" python scientific_method.py
```

### Options

- `--question`, `-q` - Specify the scientific question to investigate
- `--no-data` - Skip experimental data generation (faster, theoretical analysis only)

### Examples

```bash
# Full investigation with simulated data
python scientific_method.py "Why is the sky blue?"

# Theoretical analysis without data generation
python scientific_method.py --no-data "What is the nature of dark matter?"

# Using environment variable
export SCIENTIFIC_METHOD_QUESTION="Does coffee improve cognitive performance?"
python scientific_method.py
```

## Output

The script generates two output files:

1. **Log File** - `scientific_method_YYYYMMDD_HHMMSS.log`
   - Timestamped log with all steps and outputs
   - Human-readable format for review

2. **Results JSON** - `scientific_method_results.json`
   - Structured data containing all results
   - Can be processed programmatically

## Example Output Structure

```json
{
  "question": "Does rapamycin increase lifespan?",
  "observations": "...",
  "hypothesis": "...",
  "predictions": "...",
  "experiments": "...",
  "experimental_data": "...",
  "analysis": "...",
  "conclusion": "..."
}
```

## API Configuration

The script uses OpenAI's API. By default, it's configured for GPT-5:

```python
self.model = "gpt-5"
```

To use a different model, modify this in the `ScientificMethod.__init__` method or update the code to accept model as a parameter.

## Development

### Project Structure

```
scientific-method/
├── scientific_method.py    # Main script
├── requirements.txt        # Python dependencies
├── .env                   # API keys (not in repo)
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

### Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## License

MIT License - feel free to use this project for any purpose.

## Notes

- The observe step uses web search capabilities for gathering real-world context
- Experimental data generation is simulated by the LLM (not real experiments)
- Results quality depends on the LLM model capabilities
- Best used for theoretical investigations and research planning

## Troubleshooting

**API Key Issues:**
- Ensure your `.env` file contains a valid OpenAI API key
- Check that the key has access to the model specified

**Model Not Available:**
- If GPT-5 is not available, update the model name in the code to an available model (e.g., "gpt-4", "gpt-4-turbo")

**Import Errors:**
- Run `pip install -r requirements.txt` to install all dependencies

## Acknowledgments

Built with OpenAI's API for automated scientific reasoning and investigation planning.
