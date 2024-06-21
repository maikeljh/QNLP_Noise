import pandas as pd
import re

# Function to extract data from log lines
def extract_log_data(log_line):
    pattern = re.compile(r"train/loss: ([\d\.]+)\s+valid/loss: ([\d\.]+)\s+train/acc: ([\d\.]+)\s+valid/acc: ([\d\.]+)")
    match = pattern.search(log_line)
    if match:
        return {
            "Train Accuracy": float(match.group(3)),
            "Train Loss": float(match.group(1)),
            "Validation Accuracy": float(match.group(4)),
            "Validation Loss": float(match.group(2)),
        }
    return None

# Example log data as a single string with new line separation
log_data = """
Epoch 1:    train/loss: 5.5192   valid/loss: 4.0330   train/acc: 0.5329   valid/acc: 0.4667
Epoch 2:    train/loss: 0.5784   valid/loss: 6.1226   train/acc: 0.5461   valid/acc: 0.4500
Epoch 3:    train/loss: 4.2491   valid/loss: 4.6925   train/acc: 0.3421   valid/acc: 0.4833
Epoch 4:    train/loss: 2.6380   valid/loss: 1.4667   train/acc: 0.4276   valid/acc: 0.4833
Epoch 5:    train/loss: 1.0329   valid/loss: 2.6478   train/acc: 0.5395   valid/acc: 0.5333
Epoch 6:    train/loss: 2.2954   valid/loss: 6.0544   train/acc: 0.5066   valid/acc: 0.4167
Epoch 7:    train/loss: 7.3395   valid/loss: 5.8356   train/acc: 0.5132   valid/acc: 0.5500
Epoch 8:    train/loss: 0.8426   valid/loss: 1.8104   train/acc: 0.4803   valid/acc: 0.3500
Epoch 9:    train/loss: 0.4889   valid/loss: 2.0445   train/acc: 0.4145   valid/acc: 0.5500
Epoch 10:   train/loss: 2.8598   valid/loss: 4.5168   train/acc: 0.6053   valid/acc: 0.6000
Epoch 11:   train/loss: 0.1567   valid/loss: 3.5300   train/acc: 0.5789   valid/acc: 0.4333
Epoch 12:   train/loss: 2.3120   valid/loss: 2.0812   train/acc: 0.4342   valid/acc: 0.5333
Epoch 13:   train/loss: 4.1338   valid/loss: 4.5411   train/acc: 0.4539   valid/acc: 0.5500
Epoch 14:   train/loss: 6.1766   valid/loss: 3.7091   train/acc: 0.5329   valid/acc: 0.3333
Epoch 15:   train/loss: 2.2032   valid/loss: 3.9391   train/acc: 0.5724   valid/acc: 0.5333
Epoch 16:   train/loss: 2.1708   valid/loss: 2.6965   train/acc: 0.4079   valid/acc: 0.5500
Epoch 17:   train/loss: 3.8594   valid/loss: 5.3109   train/acc: 0.5921   valid/acc: 0.5500
Epoch 18:   train/loss: 0.9966   valid/loss: 4.9048   train/acc: 0.5855   valid/acc: 0.4333
Epoch 19:   train/loss: 2.4565   valid/loss: 2.8949   train/acc: 0.4671   valid/acc: 0.4333
Epoch 20:   train/loss: 4.0060   valid/loss: 2.6452   train/acc: 0.4803   valid/acc: 0.6000
Epoch 21:   train/loss: 0.4463   valid/loss: 3.2921   train/acc: 0.5987   valid/acc: 0.5833
Epoch 22:   train/loss: 0.5043   valid/loss: 2.7218   train/acc: 0.5526   valid/acc: 0.4667
Epoch 23:   train/loss: 0.8065   valid/loss: 1.5287   train/acc: 0.4605   valid/acc: 0.5000
Epoch 24:   train/loss: 2.3517   valid/loss: 3.3383   train/acc: 0.4868   valid/acc: 0.5333
Epoch 25:   train/loss: 5.8401   valid/loss: 4.0837   train/acc: 0.5395   valid/acc: 0.4667
Epoch 26:   train/loss: 5.6369   valid/loss: 2.7826   train/acc: 0.5395   valid/acc: 0.4500
Epoch 27:   train/loss: 0.3769   valid/loss: 3.3959   train/acc: 0.4868   valid/acc: 0.4833
Epoch 28:   train/loss: 2.6507   valid/loss: 1.9178   train/acc: 0.5526   valid/acc: 0.6667
Epoch 29:   train/loss: 0.3725   valid/loss: 4.0287   train/acc: 0.5461   valid/acc: 0.5167
Epoch 30:   train/loss: 7.4351   valid/loss: 3.2581   train/acc: 0.5855   valid/acc: 0.6167
Epoch 31:   train/loss: 0.7218   valid/loss: 2.6615   train/acc: 0.5000   valid/acc: 0.6333
Epoch 32:   train/loss: 4.4873   valid/loss: 2.7250   train/acc: 0.5395   valid/acc: 0.5500
Epoch 33:   train/loss: 0.5114   valid/loss: 4.5095   train/acc: 0.4803   valid/acc: 0.6833
Epoch 34:   train/loss: 0.8384   valid/loss: 3.3474   train/acc: 0.5197   valid/acc: 0.5000
Epoch 35:   train/loss: 0.7044   valid/loss: 2.6698   train/acc: 0.5329   valid/acc: 0.5333
Epoch 36:   train/loss: 0.6037   valid/loss: 1.5382   train/acc: 0.4408   valid/acc: 0.6333
Epoch 37:   train/loss: 4.5945   valid/loss: 4.6897   train/acc: 0.4276   valid/acc: 0.5167
Epoch 38:   train/loss: 4.0921   valid/loss: 1.4326   train/acc: 0.5329   valid/acc: 0.4167
Epoch 39:   train/loss: 4.3505   valid/loss: 5.6319   train/acc: 0.4605   valid/acc: 0.3667
Epoch 40:   train/loss: 2.3740   valid/loss: 2.1348   train/acc: 0.5000   valid/acc: 0.5000
Epoch 41:   train/loss: 4.0624   valid/loss: 2.0520   train/acc: 0.4474   valid/acc: 0.5167
Epoch 42:   train/loss: 2.3502   valid/loss: 4.6717   train/acc: 0.5197   valid/acc: 0.4667
Epoch 43:   train/loss: 2.5185   valid/loss: 3.2850   train/acc: 0.4934   valid/acc: 0.5000
Epoch 44:   train/loss: 4.2356   valid/loss: 3.4921   train/acc: 0.4474   valid/acc: 0.4833
Epoch 45:   train/loss: 2.5648   valid/loss: 1.4191   train/acc: 0.4803   valid/acc: 0.5833
Epoch 46:   train/loss: 2.1287   valid/loss: 2.2097   train/acc: 0.5724   valid/acc: 0.5667
Epoch 47:   train/loss: 2.4226   valid/loss: 2.0568   train/acc: 0.6053   valid/acc: 0.5333
Epoch 48:   train/loss: 3.8509   valid/loss: 1.3491   train/acc: 0.5724   valid/acc: 0.5667
Epoch 49:   train/loss: 2.0659   valid/loss: 1.9707   train/acc: 0.4342   valid/acc: 0.6000
Epoch 50:   train/loss: 0.8533   valid/loss: 0.7734   train/acc: 0.4211   valid/acc: 0.5500
Epoch 51:   train/loss: 2.1521   valid/loss: 5.4744   train/acc: 0.4737   valid/acc: 0.4333
Epoch 52:   train/loss: 0.6273   valid/loss: 3.1668   train/acc: 0.5461   valid/acc: 0.6667
Epoch 53:   train/loss: 0.9152   valid/loss: 0.6304   train/acc: 0.6053   valid/acc: 0.6667
Epoch 54:   train/loss: 5.6738   valid/loss: 3.3499   train/acc: 0.6053   valid/acc: 0.5333
Epoch 55:   train/loss: 5.8859   valid/loss: 1.2496   train/acc: 0.5789   valid/acc: 0.6333
Epoch 56:   train/loss: 2.5155   valid/loss: 1.4396   train/acc: 0.6184   valid/acc: 0.5500
Epoch 57:   train/loss: 0.8215   valid/loss: 2.0150   train/acc: 0.5263   valid/acc: 0.5500
Epoch 58:   train/loss: 1.1394   valid/loss: 4.8436   train/acc: 0.4342   valid/acc: 0.4000
Epoch 59:   train/loss: 0.5255   valid/loss: 3.3164   train/acc: 0.4737   valid/acc: 0.5833
Epoch 60:   train/loss: 2.2009   valid/loss: 2.6594   train/acc: 0.5789   valid/acc: 0.5667
Epoch 61:   train/loss: 2.8386   valid/loss: 3.9175   train/acc: 0.5724   valid/acc: 0.5333
Epoch 62:   train/loss: 3.8234   valid/loss: 4.0658   train/acc: 0.5066   valid/acc: 0.5000
Epoch 63:   train/loss: 4.2645   valid/loss: 5.4729   train/acc: 0.4474   valid/acc: 0.3667
Epoch 64:   train/loss: 0.7189   valid/loss: 4.6435   train/acc: 0.4737   valid/acc: 0.5333
Epoch 65:   train/loss: 0.6225   valid/loss: 2.6498   train/acc: 0.5132   valid/acc: 0.5333
Epoch 66:   train/loss: 1.0291   valid/loss: 6.2772   train/acc: 0.5066   valid/acc: 0.3333
Epoch 67:   train/loss: 0.2588   valid/loss: 2.6122   train/acc: 0.5263   valid/acc: 0.5500
Epoch 68:   train/loss: 0.7700   valid/loss: 3.4521   train/acc: 0.5395   valid/acc: 0.4167
Epoch 69:   train/loss: 1.0222   valid/loss: 1.3894   train/acc: 0.5066   valid/acc: 0.4833
Epoch 70:   train/loss: 2.5159   valid/loss: 2.7038   train/acc: 0.4474   valid/acc: 0.4833
Epoch 71:   train/loss: 2.6125   valid/loss: 4.1769   train/acc: 0.4408   valid/acc: 0.4000
Epoch 72:   train/loss: 1.0272   valid/loss: 2.2791   train/acc: 0.5921   valid/acc: 0.4500
Epoch 73:   train/loss: 6.2472   valid/loss: 1.4341   train/acc: 0.5592   valid/acc: 0.5333
Epoch 74:   train/loss: 4.4312   valid/loss: 2.7958   train/acc: 0.4276   valid/acc: 0.4167
Epoch 75:   train/loss: 7.4196   valid/loss: 0.8351   train/acc: 0.5132   valid/acc: 0.5167
Epoch 76:   train/loss: 0.7782   valid/loss: 6.1329   train/acc: 0.5000   valid/acc: 0.3667
Epoch 77:   train/loss: 0.5431   valid/loss: 6.0353   train/acc: 0.4276   valid/acc: 0.4667
Epoch 78:   train/loss: 2.8693   valid/loss: 4.0911   train/acc: 0.5855   valid/acc: 0.4500
Epoch 79:   train/loss: 5.6907   valid/loss: 3.9760   train/acc: 0.5066   valid/acc: 0.4667
Epoch 80:   train/loss: 3.9151   valid/loss: 2.6429   train/acc: 0.5329   valid/acc: 0.5667
Epoch 81:   train/loss: 4.3876   valid/loss: 4.6274   train/acc: 0.4934   valid/acc: 0.5500
Epoch 82:   train/loss: 0.8536   valid/loss: 2.9708   train/acc: 0.5263   valid/acc: 0.4167
Epoch 83:   train/loss: 6.1687   valid/loss: 3.4726   train/acc: 0.4211   valid/acc: 0.4333
Epoch 84:   train/loss: 5.5218   valid/loss: 1.4121   train/acc: 0.4605   valid/acc: 0.5667
Epoch 85:   train/loss: 2.7955   valid/loss: 0.7077   train/acc: 0.3750   valid/acc: 0.6667
Epoch 86:   train/loss: 5.9623   valid/loss: 5.4841   train/acc: 0.4803   valid/acc: 0.3833
Epoch 87:   train/loss: 0.4673   valid/loss: 3.2245   train/acc: 0.5197   valid/acc: 0.6000
Epoch 88:   train/loss: 7.2695   valid/loss: 7.4705   train/acc: 0.4868   valid/acc: 0.4000
Epoch 89:   train/loss: 1.0864   valid/loss: 2.8598   train/acc: 0.5263   valid/acc: 0.4667
Epoch 90:   train/loss: 2.5832   valid/loss: 2.8385   train/acc: 0.4211   valid/acc: 0.4333
Epoch 91:   train/loss: 0.5756   valid/loss: 2.5697   train/acc: 0.5395   valid/acc: 0.6167
Epoch 92:   train/loss: 0.8184   valid/loss: 4.7056   train/acc: 0.5855   valid/acc: 0.4500
Epoch 93:   train/loss: 4.1691   valid/loss: 6.0343   train/acc: 0.5132   valid/acc: 0.4333
Epoch 94:   train/loss: 0.6585   valid/loss: 2.6226   train/acc: 0.5132   valid/acc: 0.5667
Epoch 95:   train/loss: 0.3738   valid/loss: 4.6378   train/acc: 0.5855   valid/acc: 0.4667
Epoch 96:   train/loss: 2.3809   valid/loss: 1.5162   train/acc: 0.5132   valid/acc: 0.6167
Epoch 97:   train/loss: 4.6202   valid/loss: 2.0581   train/acc: 0.5987   valid/acc: 0.5667
Epoch 98:   train/loss: 3.9884   valid/loss: 3.2130   train/acc: 0.6053   valid/acc: 0.6500
Epoch 99:   train/loss: 5.7589   valid/loss: 3.0447   train/acc: 0.5197   valid/acc: 0.4000
Epoch 100:  train/loss: 2.2648   valid/loss: 4.6138   train/acc: 0.5789   valid/acc: 0.4833
Epoch 101:  train/loss: 0.7332   valid/loss: 2.6646   train/acc: 0.5329   valid/acc: 0.5500
Epoch 102:  train/loss: 0.6567   valid/loss: 3.8781   train/acc: 0.5658   valid/acc: 0.5833
Epoch 103:  train/loss: 0.5734   valid/loss: 2.7794   train/acc: 0.5987   valid/acc: 0.4833
Epoch 104:  train/loss: 0.6118   valid/loss: 1.3296   train/acc: 0.5263   valid/acc: 0.5333
Epoch 105:  train/loss: 0.7748   valid/loss: 0.7114   train/acc: 0.6579   valid/acc: 0.6333
Epoch 106:  train/loss: 2.4125   valid/loss: 0.7765   train/acc: 0.6842   valid/acc: 0.5000
Epoch 107:  train/loss: 5.9128   valid/loss: 2.1137   train/acc: 0.5329   valid/acc: 0.5000
Epoch 108:  train/loss: 3.9521   valid/loss: 5.2537   train/acc: 0.5329   valid/acc: 0.5667
Epoch 109:  train/loss: 3.8796   valid/loss: 2.7164   train/acc: 0.5000   valid/acc: 0.5667
Epoch 110:  train/loss: 0.7387   valid/loss: 1.2577   train/acc: 0.4671   valid/acc: 0.6500
Epoch 111:  train/loss: 2.1943   valid/loss: 2.9311   train/acc: 0.5724   valid/acc: 0.4167
Epoch 112:  train/loss: 3.9497   valid/loss: 4.1226   train/acc: 0.5592   valid/acc: 0.3833
Epoch 113:  train/loss: 4.0054   valid/loss: 2.9097   train/acc: 0.5855   valid/acc: 0.4667
Epoch 114:  train/loss: 2.3670   valid/loss: 0.7930   train/acc: 0.5395   valid/acc: 0.4500
Epoch 115:  train/loss: 0.6551   valid/loss: 4.1047   train/acc: 0.4605   valid/acc: 0.3667
Epoch 116:  train/loss: 2.9591   valid/loss: 3.3989   train/acc: 0.4868   valid/acc: 0.4167
Epoch 117:  train/loss: 2.2990   valid/loss: 4.8110   train/acc: 0.4013   valid/acc: 0.3500
Epoch 118:  train/loss: 3.9639   valid/loss: 2.0505   train/acc: 0.4605   valid/acc: 0.5833
Epoch 119:  train/loss: 0.4059   valid/loss: 1.3772   train/acc: 0.6184   valid/acc: 0.5333
Epoch 120:  train/loss: 0.5823   valid/loss: 3.2917   train/acc: 0.4803   valid/acc: 0.5833
Epoch 121:  train/loss: 0.7290   valid/loss: 3.5526   train/acc: 0.5132   valid/acc: 0.5000
Epoch 122:  train/loss: 3.9614   valid/loss: 5.0220   train/acc: 0.4539   valid/acc: 0.4000
Epoch 123:  train/loss: 2.3662   valid/loss: 3.9834   train/acc: 0.5789   valid/acc: 0.4333
Epoch 124:  train/loss: 5.3223   valid/loss: 5.9940   train/acc: 0.5526   valid/acc: 0.4667
Epoch 125:  train/loss: 5.6172   valid/loss: 5.3903   train/acc: 0.4868   valid/acc: 0.4167
Epoch 126:  train/loss: 0.5714   valid/loss: 3.0057   train/acc: 0.5132   valid/acc: 0.3833
Epoch 127:  train/loss: 0.7851   valid/loss: 2.7379   train/acc: 0.4737   valid/acc: 0.5167
Epoch 128:  train/loss: 2.8764   valid/loss: 1.9765   train/acc: 0.5789   valid/acc: 0.6167
Epoch 129:  train/loss: 5.6155   valid/loss: 4.7809   train/acc: 0.5461   valid/acc: 0.3833
Epoch 130:  train/loss: 4.2569   valid/loss: 2.7022   train/acc: 0.6053   valid/acc: 0.5000
"""

# Split the log data by new lines
log_lines = log_data.strip().split('\n')

# Extract data for each log line
data_list = [extract_log_data(line) for line in log_lines if extract_log_data(line) is not None]

# Create DataFrame
df_multiple = pd.DataFrame(data_list)

df_multiple.to_excel("result.xlsx")