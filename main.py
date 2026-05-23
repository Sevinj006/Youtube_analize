import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# dataseti oxuyuruq
data = pd.read_csv("./youtubeanaliz/yootube_data.csv")

# boş dəyərləri sil
data = data.dropna()

# engagement faizini hesablayırıq
data["engagement"] = (
    (data["likes"] + data["comments"]) / data["views"]
) * 100

# ümumi statistikalar
total_views = data["views"].sum()
total_likes = data["likes"].sum()
total_comments = data["comments"].sum()

print("Toplam views:", total_views)
print("Toplam likes:", total_likes)
print("Toplam comments:", total_comments)

# qrafik stilləri
sns.set_style("darkgrid")

# ======================
# Kateqoriya üzrə views
# ======================

category_data = (
    data.groupby("category")["views"]
    .sum()
    .reset_index()
)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=category_data["category"],
    y=category_data["views"]
)

plt.title("Kateqoriyalara görə baxış sayı")
plt.xticks(rotation=25)

plt.show()

# ======================
# Ən çox izlənən videolar
# ======================

top5 = data.sort_values(
    by="views",
    ascending=False
).head(5)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=top5["views"],
    y=top5["title"]
)

plt.title("Ən çox baxılan 5 video")

plt.show()

# ======================
# Views və Likes əlaqəsi
# ======================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=data,
    x="views",
    y="likes",
    hue="category"
)

plt.title("Views və Likes əlaqəsi")

plt.show()

# ======================
# Korelasiya heatmap
# ======================

corr_data = data[
    ["views", "likes", "comments", "engagement"]
].corr()

plt.figure(figsize=(6, 4))

sns.heatmap(
    corr_data,
    annot=True,
    cmap="coolwarm"
)

plt.title("Məlumatların korelasiyası")

plt.show()