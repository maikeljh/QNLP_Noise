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
Epoch 1:    train/loss: 0.4342   valid/loss: 4.6057   train/acc: 0.5132   valid/acc: 0.5833
Epoch 2:    train/loss: 0.8793   valid/loss: 2.8329   train/acc: 0.6250   valid/acc: 0.5000
Epoch 3:    train/loss: 5.5476   valid/loss: 4.1520   train/acc: 0.6250   valid/acc: 0.4333
Epoch 4:    train/loss: 2.4353   valid/loss: 2.6954   train/acc: 0.5592   valid/acc: 0.5833
Epoch 5:    train/loss: 0.7481   valid/loss: 2.1171   train/acc: 0.6053   valid/acc: 0.4667
Epoch 6:    train/loss: 2.5505   valid/loss: 1.3761   train/acc: 0.5592   valid/acc: 0.4667
Epoch 7:    train/loss: 7.3462   valid/loss: 4.0135   train/acc: 0.4737   valid/acc: 0.4667
Epoch 8:    train/loss: 0.6567   valid/loss: 1.9635   train/acc: 0.5461   valid/acc: 0.6000
Epoch 9:    train/loss: 0.9449   valid/loss: 0.9319   train/acc: 0.5724   valid/acc: 0.4833
Epoch 10:   train/loss: 0.8155   valid/loss: 0.7554   train/acc: 0.5789   valid/acc: 0.5667
Epoch 11:   train/loss: 3.9245   valid/loss: 2.4921   train/acc: 0.5987   valid/acc: 0.7167
Epoch 12:   train/loss: 2.5059   valid/loss: 1.5007   train/acc: 0.5592   valid/acc: 0.4833
Epoch 13:   train/loss: 3.8727   valid/loss: 1.3120   train/acc: 0.4605   valid/acc: 0.6000
Epoch 14:   train/loss: 4.3261   valid/loss: 0.9787   train/acc: 0.5724   valid/acc: 0.4333
Epoch 15:   train/loss: 2.2862   valid/loss: 1.4861   train/acc: 0.5395   valid/acc: 0.5333
Epoch 16:   train/loss: 3.7830   valid/loss: 3.4138   train/acc: 0.5658   valid/acc: 0.5500
Epoch 17:   train/loss: 0.7540   valid/loss: 4.0768   train/acc: 0.5263   valid/acc: 0.4333
Epoch 18:   train/loss: 4.3152   valid/loss: 5.2513   train/acc: 0.4803   valid/acc: 0.5167
Epoch 19:   train/loss: 0.6226   valid/loss: 3.3162   train/acc: 0.5263   valid/acc: 0.5000
Epoch 20:   train/loss: 0.6357   valid/loss: 2.7489   train/acc: 0.5724   valid/acc: 0.4667
Epoch 21:   train/loss: 0.4669   valid/loss: 1.1863   train/acc: 0.6382   valid/acc: 0.7000
Epoch 22:   train/loss: 2.9487   valid/loss: 2.1067   train/acc: 0.6118   valid/acc: 0.5500
Epoch 23:   train/loss: 0.8802   valid/loss: 2.0965   train/acc: 0.6250   valid/acc: 0.4833
Epoch 24:   train/loss: 5.6591   valid/loss: 3.3698   train/acc: 0.5461   valid/acc: 0.4500
Epoch 25:   train/loss: 3.9677   valid/loss: 2.8752   train/acc: 0.5592   valid/acc: 0.3833
Epoch 26:   train/loss: 0.6011   valid/loss: 3.4228   train/acc: 0.4934   valid/acc: 0.4333
Epoch 27:   train/loss: 0.5479   valid/loss: 1.2118   train/acc: 0.5132   valid/acc: 0.6667
Epoch 28:   train/loss: 3.9579   valid/loss: 2.0965   train/acc: 0.6250   valid/acc: 0.4667
Epoch 29:   train/loss: 2.1887   valid/loss: 1.2932   train/acc: 0.5526   valid/acc: 0.5333
Epoch 30:   train/loss: 5.6009   valid/loss: 4.0082   train/acc: 0.4474   valid/acc: 0.5833
Epoch 31:   train/loss: 1.1228   valid/loss: 1.3213   train/acc: 0.5000   valid/acc: 0.6000
Epoch 32:   train/loss: 2.7234   valid/loss: 3.2830   train/acc: 0.4934   valid/acc: 0.6333
Epoch 33:   train/loss: 2.5421   valid/loss: 3.4843   train/acc: 0.6184   valid/acc: 0.3667
Epoch 34:   train/loss: 0.8548   valid/loss: 0.8219   train/acc: 0.4671   valid/acc: 0.4333
Epoch 35:   train/loss: 0.6978   valid/loss: 3.9837   train/acc: 0.5132   valid/acc: 0.4833
Epoch 36:   train/loss: 2.3520   valid/loss: 2.1512   train/acc: 0.5263   valid/acc: 0.5000
Epoch 37:   train/loss: 1.0815   valid/loss: 0.7863   train/acc: 0.4605   valid/acc: 0.4833
Epoch 38:   train/loss: 0.5704   valid/loss: 1.3309   train/acc: 0.5724   valid/acc: 0.6333
Epoch 39:   train/loss: 2.1995   valid/loss: 3.9377   train/acc: 0.5855   valid/acc: 0.5667
Epoch 40:   train/loss: 0.6684   valid/loss: 1.2976   train/acc: 0.6118   valid/acc: 0.5667
Epoch 41:   train/loss: 0.6071   valid/loss: 3.3466   train/acc: 0.5592   valid/acc: 0.4833
Epoch 42:   train/loss: 2.3944   valid/loss: 3.5551   train/acc: 0.5000   valid/acc: 0.4667
Epoch 43:   train/loss: 2.6144   valid/loss: 0.7020   train/acc: 0.5329   valid/acc: 0.5833
Epoch 44:   train/loss: 2.2526   valid/loss: 2.1491   train/acc: 0.4803   valid/acc: 0.4833
Epoch 45:   train/loss: 0.7224   valid/loss: 1.4655   train/acc: 0.4671   valid/acc: 0.6000
Epoch 46:   train/loss: 7.0928   valid/loss: 3.4147   train/acc: 0.4803   valid/acc: 0.5833
Epoch 47:   train/loss: 0.6972   valid/loss: 0.7310   train/acc: 0.4671   valid/acc: 0.4833
Epoch 48:   train/loss: 4.1589   valid/loss: 6.0100   train/acc: 0.4803   valid/acc: 0.4833
Epoch 49:   train/loss: 2.7412   valid/loss: 1.5042   train/acc: 0.4737   valid/acc: 0.5500
Epoch 50:   train/loss: 0.7581   valid/loss: 2.2213   train/acc: 0.6382   valid/acc: 0.5000
Epoch 51:   train/loss: 5.8922   valid/loss: 5.2945   train/acc: 0.4868   valid/acc: 0.5333
Epoch 52:   train/loss: 0.5802   valid/loss: 3.8547   train/acc: 0.6645   valid/acc: 0.5667
Epoch 53:   train/loss: 0.6373   valid/loss: 1.4619   train/acc: 0.5132   valid/acc: 0.4167
Epoch 54:   train/loss: 0.4566   valid/loss: 0.6999   train/acc: 0.6053   valid/acc: 0.5000
Epoch 55:   train/loss: 5.7043   valid/loss: 1.6460   train/acc: 0.6513   valid/acc: 0.2333
Epoch 56:   train/loss: 2.6433   valid/loss: 3.3777   train/acc: 0.5789   valid/acc: 0.4500
Epoch 57:   train/loss: 2.4441   valid/loss: 2.2515   train/acc: 0.5197   valid/acc: 0.4667
Epoch 58:   train/loss: 0.6799   valid/loss: 2.9169   train/acc: 0.6118   valid/acc: 0.4000
Epoch 59:   train/loss: 2.0943   valid/loss: 2.7536   train/acc: 0.5132   valid/acc: 0.5000
Epoch 60:   train/loss: 3.9891   valid/loss: 3.4970   train/acc: 0.3816   valid/acc: 0.5000
Epoch 61:   train/loss: 5.6626   valid/loss: 1.3850   train/acc: 0.4868   valid/acc: 0.5667
Epoch 62:   train/loss: 0.7408   valid/loss: 2.5342   train/acc: 0.6250   valid/acc: 0.6833
Epoch 63:   train/loss: 0.5298   valid/loss: 3.3309   train/acc: 0.5526   valid/acc: 0.5333
Epoch 64:   train/loss: 3.7654   valid/loss: 1.3392   train/acc: 0.6382   valid/acc: 0.6500
Epoch 65:   train/loss: 0.9675   valid/loss: 1.9399   train/acc: 0.4408   valid/acc: 0.5833
Epoch 66:   train/loss: 2.5208   valid/loss: 0.8136   train/acc: 0.4605   valid/acc: 0.5333
Epoch 67:   train/loss: 0.5504   valid/loss: 1.5023   train/acc: 0.5855   valid/acc: 0.6000
Epoch 68:   train/loss: 2.4142   valid/loss: 1.9573   train/acc: 0.5987   valid/acc: 0.6167
Epoch 69:   train/loss: 4.4246   valid/loss: 3.3418   train/acc: 0.5066   valid/acc: 0.4833
Epoch 70:   train/loss: 2.8180   valid/loss: 2.1445   train/acc: 0.5197   valid/acc: 0.4500
Epoch 71:   train/loss: 0.5786   valid/loss: 3.4171   train/acc: 0.5197   valid/acc: 0.4833
Epoch 72:   train/loss: 7.1593   valid/loss: 0.5888   train/acc: 0.5329   valid/acc: 0.7000
Epoch 73:   train/loss: 0.7458   valid/loss: 2.1768   train/acc: 0.5526   valid/acc: 0.4167
Epoch 74:   train/loss: 7.3690   valid/loss: 2.0050   train/acc: 0.4868   valid/acc: 0.5167
Epoch 75:   train/loss: 3.8965   valid/loss: 2.7114   train/acc: 0.4868   valid/acc: 0.5667
Epoch 76:   train/loss: 2.4982   valid/loss: 3.3450   train/acc: 0.5987   valid/acc: 0.5833
Epoch 77:   train/loss: 2.3346   valid/loss: 2.0460   train/acc: 0.5066   valid/acc: 0.5333
Epoch 78:   train/loss: 2.1939   valid/loss: 3.4742   train/acc: 0.5395   valid/acc: 0.4333
Epoch 79:   train/loss: 2.2532   valid/loss: 2.7248   train/acc: 0.4803   valid/acc: 0.5167
Epoch 80:   train/loss: 4.1266   valid/loss: 1.9928   train/acc: 0.5789   valid/acc: 0.6167
Epoch 81:   train/loss: 2.3142   valid/loss: 6.0927   train/acc: 0.5263   valid/acc: 0.3833
Epoch 82:   train/loss: 0.9877   valid/loss: 3.5737   train/acc: 0.4342   valid/acc: 0.5333
Epoch 83:   train/loss: 4.0346   valid/loss: 2.6433   train/acc: 0.5855   valid/acc: 0.6167
Epoch 84:   train/loss: 2.2839   valid/loss: 2.7257   train/acc: 0.5855   valid/acc: 0.4833
Epoch 85:   train/loss: 1.0245   valid/loss: 2.0737   train/acc: 0.5987   valid/acc: 0.6000
Epoch 86:   train/loss: 5.8585   valid/loss: 4.7728   train/acc: 0.5461   valid/acc: 0.4667
Epoch 87:   train/loss: 0.6675   valid/loss: 2.1287   train/acc: 0.5395   valid/acc: 0.4667
Epoch 88:   train/loss: 2.4930   valid/loss: 4.0714   train/acc: 0.5066   valid/acc: 0.3833
Epoch 89:   train/loss: 7.7364   valid/loss: 2.0107   train/acc: 0.5132   valid/acc: 0.5333
Epoch 90:   train/loss: 0.9026   valid/loss: 3.4231   train/acc: 0.5395   valid/acc: 0.4500
Epoch 91:   train/loss: 1.1912   valid/loss: 2.7046   train/acc: 0.4934   valid/acc: 0.5333
Epoch 92:   train/loss: 2.3539   valid/loss: 2.1079   train/acc: 0.4934   valid/acc: 0.5000
Epoch 93:   train/loss: 4.3325   valid/loss: 1.3391   train/acc: 0.4671   valid/acc: 0.4333
Epoch 94:   train/loss: 0.5464   valid/loss: 0.9348   train/acc: 0.5132   valid/acc: 0.4667
Epoch 95:   train/loss: 0.7401   valid/loss: 1.4914   train/acc: 0.5132   valid/acc: 0.5500
Epoch 96:   train/loss: 2.2845   valid/loss: 2.6522   train/acc: 0.5132   valid/acc: 0.5333
Epoch 97:   train/loss: 5.8537   valid/loss: 0.7728   train/acc: 0.5000   valid/acc: 0.5333
Epoch 98:   train/loss: 6.1804   valid/loss: 2.8559   train/acc: 0.4803   valid/acc: 0.4167
Epoch 99:   train/loss: 2.1025   valid/loss: 4.7933   train/acc: 0.5329   valid/acc: 0.4333
Epoch 100:  train/loss: 5.6632   valid/loss: 0.8031   train/acc: 0.4934   valid/acc: 0.5333
Epoch 101:  train/loss: 2.4804   valid/loss: 2.2549   train/acc: 0.4013   valid/acc: 0.4000
Epoch 102:  train/loss: 0.6688   valid/loss: 3.3415   train/acc: 0.5066   valid/acc: 0.5500
Epoch 103:  train/loss: 0.6002   valid/loss: 3.4136   train/acc: 0.5000   valid/acc: 0.5000
Epoch 104:  train/loss: 0.4695   valid/loss: 2.2694   train/acc: 0.4474   valid/acc: 0.4500
Epoch 105:  train/loss: 0.5261   valid/loss: 1.6014   train/acc: 0.4013   valid/acc: 0.4167
Epoch 106:  train/loss: 2.3385   valid/loss: 0.9385   train/acc: 0.5395   valid/acc: 0.4000
Epoch 107:  train/loss: 2.5339   valid/loss: 1.9927   train/acc: 0.3947   valid/acc: 0.5833
Epoch 108:  train/loss: 2.2572   valid/loss: 2.1028   train/acc: 0.6118   valid/acc: 0.5500
Epoch 109:  train/loss: 0.4923   valid/loss: 2.7205   train/acc: 0.4934   valid/acc: 0.5500
Epoch 110:  train/loss: 8.9569   valid/loss: 0.7128   train/acc: 0.5855   valid/acc: 0.6000
Epoch 111:  train/loss: 2.3825   valid/loss: 1.4291   train/acc: 0.5658   valid/acc: 0.5000
Epoch 112:  train/loss: 5.9296   valid/loss: 5.4370   train/acc: 0.5000   valid/acc: 0.4000
Epoch 113:  train/loss: 0.5739   valid/loss: 2.2426   train/acc: 0.4474   valid/acc: 0.3833
Epoch 114:  train/loss: 0.6782   valid/loss: 2.7875   train/acc: 0.4408   valid/acc: 0.5000
Epoch 115:  train/loss: 0.7793   valid/loss: 2.7089   train/acc: 0.4737   valid/acc: 0.5333
Epoch 116:  train/loss: 5.6850   valid/loss: 4.2471   train/acc: 0.5197   valid/acc: 0.3500
Epoch 117:  train/loss: 1.1355   valid/loss: 0.8904   train/acc: 0.5526   valid/acc: 0.4500
Epoch 118:  train/loss: 4.1006   valid/loss: 2.7506   train/acc: 0.5263   valid/acc: 0.4667
Epoch 119:  train/loss: 2.0844   valid/loss: 2.2716   train/acc: 0.5329   valid/acc: 0.4500
Epoch 120:  train/loss: 4.1960   valid/loss: 2.4431   train/acc: 0.4211   valid/acc: 0.4167
Epoch 121:  train/loss: 0.6541   valid/loss: 1.4619   train/acc: 0.5263   valid/acc: 0.4833
Epoch 122:  train/loss: 0.5106   valid/loss: 1.9675   train/acc: 0.4868   valid/acc: 0.6500
Epoch 123:  train/loss: 1.1986   valid/loss: 0.8666   train/acc: 0.5066   valid/acc: 0.5167
Epoch 124:  train/loss: 4.4030   valid/loss: 2.0903   train/acc: 0.4079   valid/acc: 0.5333
Epoch 125:  train/loss: 0.7470   valid/loss: 2.2041   train/acc: 0.4868   valid/acc: 0.4833
Epoch 126:  train/loss: 0.9883   valid/loss: 1.9386   train/acc: 0.4737   valid/acc: 0.6000
Epoch 127:  train/loss: 4.3741   valid/loss: 2.2435   train/acc: 0.5197   valid/acc: 0.4167
Epoch 128:  train/loss: 0.6917   valid/loss: 3.4174   train/acc: 0.5855   valid/acc: 0.5167
Epoch 129:  train/loss: 1.0469   valid/loss: 2.8810   train/acc: 0.4211   valid/acc: 0.3500
Epoch 130:  train/loss: 3.9251   valid/loss: 2.0063   train/acc: 0.5658   valid/acc: 0.5833
"""

# Split the log data by new lines
log_lines = log_data.strip().split('\n')

# Extract data for each log line
data_list = [extract_log_data(line) for line in log_lines if extract_log_data(line) is not None]

# Create DataFrame
df_multiple = pd.DataFrame(data_list)

df_multiple.to_excel("result.xlsx")