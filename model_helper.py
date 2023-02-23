from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import f1_score
from imblearn.over_sampling import SMOTE

def model_helper(X, y, model, feature_importance = False):
    """
    Helper function to run sklearn models.  
    
    Args:
        X (dataframe): Features to train on. 
        y (series): Target variable
        model (sklearn): Model to train on.
        feature_importance (bool): True equals plot feature importance table. 
        
    Returns:
        model (sklearn): Trained model
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = 86)
    
    # Apply SMOTE to the training data
    sm = SMOTE(random_state=86)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

    # Fit the model to the training data
    model.fit(X_train_res, y_train_res)

    # Make predictions on the training and testing data
    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    # Calculate the F1 score for training and testing
    f1_train = f1_score(y_train, y_train_pred)
    f1_test = f1_score(y_test, y_test_pred)

    # Output the scores to the console
    print("Training Score:", model.score(X_train, y_train))
    print("Testing Score:", model.score(X_test, y_test))
    print("F1 Score (Training):", f1_train)
    print("F1 Score (Testing):", f1_test)
    
    if feature_importance:
        feat_import = pd.DataFrame({"features": X_train.columns, "importance": model.feature_importances_})
        print(feat_import.sort_values("importance", ascending=False))
    return model
