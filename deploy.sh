#!/bin/bash

# GearGuard Deployment Script
echo "🚀 Deploying GearGuard to Production..."

# Check if we're in the right directory
if [ ! -f "manage.py" ]; then
    echo "❌ Error: manage.py not found. Please run from project root."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Check if superuser exists (optional)
echo "👤 Checking for superuser..."
python manage.py shell -c "from django.contrib.auth.models import User; print('Superuser exists' if User.objects.filter(is_superuser=True).exists() else 'No superuser found')"

echo "✅ Deployment setup complete!"
echo ""
echo "🌐 Next steps:"
echo "1. Set environment variables:"
echo "   export DJANGO_SECRET_KEY='$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
echo "   export DEBUG=False"
echo "   export ALLOWED_HOSTS='yourdomain.com'"
echo "   export DATABASE_URL='postgresql://user:pass@host:port/dbname'"
echo ""
echo "2. Run the server:"
echo "   gunicorn gearguard.wsgi --bind 0.0.0.0:8000"
echo ""
echo "3. For production, use a process manager like systemd or supervisor"
