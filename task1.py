import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return df.columns.tolist()

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df.type.unique().tolist()

def exercise_5(df):
    return df.nameDest.value_counts().head(10)

def exercise_6(df):
    return df[df.isFraud == 1]

def exercise_7(df):
    df_groupby_name_dest = df.groupby("nameDest")["newbalanceDest"].agg("mean")
    df_sorted_values = df_groupby_name_dest.sort_values(ascending=False)
    return df_sorted_values

def visual_1(df):
    def transaction_counts(df):
        return df.type.value_counts()
    def transaction_counts_split_by_fraud(df):
        filtered_df = df[df['isFraud'] == 1]
        frequency_counts = filtered_df['type'].value_counts()
        return frequency_counts

    fig, axs = plt.subplots(2, figsize=(6,10))

    transaction_counts(df).plot(ax=axs[0], kind='bar', width=0.6, rot=90)
    axs[0].set_title('Transaction Counts')
    axs[0].set_xlabel('Transaction Type')
    axs[0].set_ylabel('Count')
    plt.xticks(rotation=0)
    axs[0].set_xticklabels(axs[0].get_xticklabels(), rotation=0)
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar', width=0.2)
    axs[1].set_title('Transaction Counts for Fraudulent Transactions')
    axs[1].set_xlabel('Transaction Type')
    axs[1].set_ylabel('Count')
    axs[1].set_xticklabels(axs[1].get_xticklabels(), rotation=0)
    fig.suptitle('Transaction Analysis')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.subplots_adjust(hspace=0.5)

    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    plt.show()
    return 'The chart displaying transaction types and the number of fraudulent transactions is relevant as it helps identify patterns in fraud and assess the risk associated with different transaction types.'

def visual_2(df):
    def query(df):
        temp_df = df[df['type'] == 'CASH_OUT'].copy()
        column1 = temp_df['oldbalanceOrg'] - temp_df['newbalanceOrig']
        column2 = temp_df['oldbalanceDest'] - temp_df['newbalanceDest']
        new_df = pd.DataFrame({'OriginAccount Balance Delta': column1, 'DestinationAccount Balance Delta': column2})
        print(new_df)
        return new_df

    new_df = query(df)
    plot = new_df.plot.scatter(x='OriginAccount Balance Delta', y='DestinationAccount Balance Delta')
    plot.set_title('Balance Delta Scatter Plot')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    plt.show()
    return 'Understanding the scatter plot depicting the relationship between the delta of origin account balance and destination account balance for Cash Out transactions is critical because it enables the detection of potential irregularities or instances of fraudulent behaviour within the financial ecosystem.'


def exercise_custom(df, step):
    step_data = df[df['step'] == step]
    type_counts = step_data['type'].value_counts().reset_index()
    type_counts.columns = ['type', 'frequency']
    
    all_types = df['type'].unique()
    missing_types = list(set(all_types) - set(type_counts['type']))
    missing_counts = pd.DataFrame({'type': missing_types, 'frequency': 0})
    
    step_df = pd.concat([type_counts, missing_counts], ignore_index=True)
    return step_df
    
def visual_custom(df, step):
    step_df = exercise_custom(df, step)
    
    labels = step_df['type']
    frequencies = step_df['frequency']
    
    plt.pie(frequencies, labels=labels, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title(f'Pie Chart for Step {step}')
    plt.show()
    return ''