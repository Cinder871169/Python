import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Đọc dữ liệu từ các file CSV
flights = pd.read_csv("flights.csv")
salaries = pd.read_csv("Salaries.csv")


def statistics_for_column(df, column_name):
    if column_name in df.columns and pd.api.types.is_numeric_dtype(df[column_name]):
        max_val = df[column_name].max()
        min_val = df[column_name].min()
        mean_val = df[column_name].mean()

        print(f"{column_name}:")
        print(f"  Max value: {max_val}")
        print(f"  Min value: {min_val}")
        print(f"  Mean value: {mean_val}")

        # Vẽ biểu đồ scatter
        plt.figure(figsize=(10, 6))
        plt.scatter(df.index, df[column_name], alpha=0.5)
        plt.title(f"Scatter plot of {column_name}")
        plt.xlabel("Index")
        plt.ylabel(column_name)
        plt.show()
    else:
        print(
            f'Column "{column_name}" is not numeric or does not exist in the dataframe.'
        )


def plot_day_month_distance(flights):
    # Tạo cột datetime từ year, month, day
    flights["date"] = pd.to_datetime(flights[["year", "month", "day"]])

    plt.figure(figsize=(12, 6))
    sns.lineplot(x="date", y="distance", data=flights, marker="o")
    plt.title("Distance over time")
    plt.xlabel("Date")
    plt.ylabel("Distance")
    plt.xticks(rotation=45)
    plt.show()


def plot_sex_distribution(salaries):
    plt.figure(figsize=(8, 5))
    sns.countplot(x="sex", data=salaries)
    plt.title("Distribution of Sex in Salaries")
    plt.xlabel("Sex")
    plt.ylabel("Count")
    plt.show()


def sort_and_plot(df, column_name):
    if column_name in df.columns:
        sorted_df = df.sort_values(by=column_name)

        # Vẽ biểu đồ
        plt.figure(figsize=(10, 6))

        # Nếu cột là kiểu số, sử dụng scatter plot
        if pd.api.types.is_numeric_dtype(df[column_name]):
            plt.scatter(sorted_df.index, sorted_df[column_name], alpha=0.5)
            plt.title(f"Scatter plot of {column_name} (sorted)")
            plt.xlabel("Index")
            plt.ylabel(column_name)
        else:
            # Nếu cột không phải số, sử dụng countplot
            sns.countplot(x=column_name, data=sorted_df)
            plt.title(f"Count plot of {column_name} (sorted)")
            plt.xlabel(column_name)
            plt.ylabel("Count")

        plt.show()
    else:
        print(f'Column "{column_name}" does not exist in the dataframe.')


def main():
    while True:
        print("\nOptions:")
        print("1. Statistics for a column (Flights or Salaries)")
        print("2. Plot day-month-distance (Flights.csv)")
        print("3. Plot sex distribution (Salaries.csv)")
        print("4. Sort and plot by column")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            dataset = input("Choose dataset (Flights/Salaries): ").strip().lower()
            column_name = input("Enter the column name: ").strip()

            if dataset == "flights":
                statistics_for_column(flights, column_name)
            elif dataset == "salaries":
                statistics_for_column(salaries, column_name)
            else:
                print("Invalid dataset choice.")

        elif choice == "2":
            plot_day_month_distance(flights)

        elif choice == "3":
            plot_sex_distribution(salaries)

        elif choice == "4":
            dataset = input("Choose dataset (Flights/Salaries): ").strip().lower()
            column_name = input("Enter the column name to sort by: ").strip()

            if dataset == "flights":
                sort_and_plot(flights, column_name)
            elif dataset == "salaries":
                sort_and_plot(salaries, column_name)
            else:
                print("Invalid dataset choice.")

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
