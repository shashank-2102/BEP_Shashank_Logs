# LLM Log Parsing BEP - Shashank Prabh BDS TU/e and TiU
Github Repo for BEP Shashank Prabhu (BDS)

**Good to know:**
- Some parts of the code use a proprietary API getter. Comment out or remove before using (and supply your own Gemini API key - you can get one from Google AI Studio).
The same goes for VPN. At the time of starting, the API was not available within the EU, so a VPN was needed.
- Code still uses absolute paths in some cases :/

**Files and Purpose (sort of in the order you should run them in):**
- **dataset_injection_multi (notebook)** - Takes df and uses LLM to create augmented templates at 4 different levels + original.
- **dataset_var_insertion (notebook)** - Adds variables to wildcards <*> for the injected log templates, 31 each.
- **add_prefix (notebook)** - Based on collected prefixes, just add them to the augmented templates (at the start).
- **llm_log_parser_complete (notebook)** - Contains file code, including prompt templates for the final LLM parser.
- **eval_metrics (notebook)** - Contains code for all eval metrics and most of the graphs used in the thesis (useD Loghub 2.0 based code for metrics).

**(You don't actually run these):**
- **clustering (py)** - Contains code that takes in logs df and generates n most representative logs.
- **vpn_control (py)** - Contains VPN control code (CLI) - code from an external source.
