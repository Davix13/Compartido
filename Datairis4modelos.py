# Importar las bibliotecas necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Cargar el conjunto de datos Iris
iris = load_iris()
x = iris.data
y = iris.target

# Inicializar los modelos
models = {
    "Regresión Logística": LogisticRegression(max_iter=1000),
    "SVM": SVC(),
    "Árbol de Decisión": DecisionTreeClassifier(),
    "Bosque Aleatorio": RandomForestClassifier()
}

# Realizar validación cruzada para cada modelo
for model_name, model in models.items():
    print(model_name)
    
    # Realizar predicciones con validación cruzada
    y_pred = cross_val_predict(model, x, y, cv=5)
    
    # Calcular la matriz de confusión
    conf_matrix = confusion_matrix(y, y_pred)
    print("Matriz de Confusión:")
    print(conf_matrix)
    
    # Calcular y imprimir las métricas de evaluación
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred, average='macro')
    recall = recall_score(y, y_pred, average='macro')
    
    print("Exactitud:", accuracy)
    print("Precisión:", precision)
    print("Exhaustividad:", recall)
    print("\n")

