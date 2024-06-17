# GitHub_Actions_BEP
Github Repo for BEP Shashank Prabhu (BDS)

Good to know:
    Some parts of the code use a propiatery API getter, comment out or remove before using (and supply own Gemini API key - you can get one from google AI Studio)

    Same goes for VPN. At the time of starting API was not available with EU so a VPN was needed.

    Cose still uses absoluate paths in soem cases :/

Files and Purpose (sort of in the order you should run them in):

    dataset_injection_multi (notebook) - takes df and uses LLM to create augmented templates at 4 different levels + original
    dataset_var_insertion (notebook) - adds variables to wildcards <*> for the injected log templates, 31 each.
    add_prefix (notebook) - based on collected prefixes just adds them to the augmented templates (at the start)
    llm_log_parser_complete (notebook) - contains file code, including promt templates for final LLM parser
    eval_metrics (notebook) - contains code for all eval metrics and most of the graphs used in the thesis (use loghub 2.0 based code for metrics)

    (you dont actually run these):
    clustering (py) - contains code that takes in logs df and generates n most representative logs
    vpn_control (py) - contains VPN control code (CLI) - code from external soruce

    
   