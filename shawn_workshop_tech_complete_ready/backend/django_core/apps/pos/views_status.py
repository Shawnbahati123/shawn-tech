from django.http import JsonResponse
from .models import Sale

def sale_status(request):
    invoice = request.GET.get('invoice_no')
    try:
        s = Sale.objects.get(invoice_no=invoice)
        return JsonResponse({'invoice_no': s.invoice_no, 'status': 'paid' if getattr(s,'paid',False) else 'pending'})
    except Sale.DoesNotExist:
        return JsonResponse({'error':'not found'}, status=404)
