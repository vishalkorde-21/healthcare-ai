from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer
from .ml_model import predict_disease
from drf_yasg.utils import swagger_auto_schema
from .ml_model import predict_disease, bert_analysis, rag_pipeline, llm_generate

@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)


@swagger_auto_schema(
    method='POST',
    request_body=PatientSerializer
)



@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)

    if serializer.is_valid():
        symptoms = serializer.validated_data['symptoms']

        # ML Prediction
        result = predict_disease(symptoms)

        diagnosis = result.get("diagnosis","unknown")
        context = result.get("context","No context availabel")

        # BERT (fake)
        bert_data = bert_analysis(symptoms)

        

        # LLM (fake)
        treatment = llm_generate(diagnosis)

        serializer.save(
            diagnosis=diagnosis,
            treatment=treatment
        )

        return Response({
            "diagnosis": diagnosis,
            "bert": bert_data,
            "context": context,
            "treatment": treatment
        })

    return Response(serializer.errors)